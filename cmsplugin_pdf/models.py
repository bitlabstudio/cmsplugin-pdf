"""Models for the ``cmsplugin_pdf`` app."""
import glob
import os

from django.conf import settings as django_settings
from django.core.files import File
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from wand.image import Image

from . import settings


UPLOAD_TO_DIR = 'pdf_images'


class PDFPluginModel(CMSPlugin):
    """
    Plugin model to link to a specific pdf file instance and its image.

    :display_type: String representing a display type. This is helpful if
      you want to render the plugin differently in different parts of your
      site.
    :file: FK to the FilerFile. Should be the PDF that is to be added.
    :image: The generated cover image from the pdf.

    """
    display_type = models.CharField(
        max_length=256,
        choices=settings.DISPLAY_TYPE_CHOICES,
        verbose_name=_('Display type'),
    )

    file = FilerFileField(
        verbose_name=_('File'),
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=UPLOAD_TO_DIR,
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
        img = Image(filename=self.file.path + '[0]')

        # make new filename
        filename = os.path.basename(self.file.path).split('.')[:-1]
        if type(filename) == list:
            filename = ''.join(filename)

        # TODO: Would be better to compute this path from the upload_to
        # setting which is already set on the model field
        image_dir = os.path.join(
            django_settings.MEDIA_ROOT, UPLOAD_TO_DIR)
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        image_path = os.path.join(
            image_dir, '{}.jpg'.format(filename))
        tmp_image_path = os.path.join(
            image_dir, '{}.tmp.jpg'.format(filename))

        # we remove the old image befor we save because the cover might have
        # changed when we upload a new PDF file - even when that file has the
        # same filename as the old one
        try:
            os.remove(image_path)
        except OSError:
            # file is already gone
            pass
        # and we also remove the thumbnails
        old_files = glob.glob('{}.*'.format(image_path))
        for old_file in old_files:
            try:
                os.remove(old_file)
            except OSError:
                pass

        # save as image under a temporary filename so that we can read it with
        # File()
        img.save(filename=tmp_image_path)
        # attach it to image field
        with open(tmp_image_path, 'r') as f:
            self.image.save('{}.jpg'.format(filename), File(f), save=False)
        super(PDFPluginModel, self).save(*args, **kwargs)

        # remove temp file
        try:
            os.remove(tmp_image_path)
        except OSError:
            pass
