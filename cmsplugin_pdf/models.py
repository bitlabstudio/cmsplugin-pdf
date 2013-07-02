"""Models for the ``cmsplugin_pdf`` app."""
import os

from django.conf import settings
from django.core.files import File
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from wand.image import Image


class PDFPluginModel(CMSPlugin):
    """
    Plugin model to link to a specific pdf file instance and its image.

    :file: FK to the FilerFile. Should be the PDF that is to be added.
    :image: The generated cover image from the pdf.

    """
    file = FilerFileField(
        verbose_name=_('File'),
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=os.path.join(settings.MEDIA_ROOT, 'pdf_images'),
        blank=True, null=True,
        editable=False,
    )

    def __unicode__(self):
        if self.file.name:
            return self.file.name
        elif self.file.original_filename:
            return self.file.original_filename
        else:
            return self.file.path

    def save(self, *args, **kwargs):
        """Customized to generate an image from the pdf file."""
        # open image from pdf
        img = Image(filename=self.file.path)
        # make new filename
        filename = os.path.basename(self.file.path).split('.')[:-1]
        if type(filename) == list:
            filename = ''.join(filename)
        image_path = os.path.join(
            settings.MEDIA_ROOT, 'pdf_images', '{}.jpg'.format(filename))
        # save as image under new filename
        img.save(filename=image_path)
        # attach it to image field
        with open(image_path, 'r') as f:
            self.image.save(filename, File(f), save=False)
        super(PDFPluginModel, self).save(*args, **kwargs)
