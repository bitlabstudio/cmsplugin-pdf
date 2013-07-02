"""Models for the ``cmsplugin_pdf`` app."""
import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField


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
    )

    def save(self, *args, **kwargs):
        """Customized to generate an image from the pdf file."""
        # TODO create image here
        return super(PDFPluginModel, self).save(*args, **kwargs)
