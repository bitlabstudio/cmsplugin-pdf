"""Settings for the cmsplugin_pdf  app."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


display_type_choices = [
    ('standard', _('standard')),
    ('small', _('small')),
    ('highlight', _('highlight')),
]

DISPLAY_TYPE_CHOICES = getattr(
    settings, 'CMSPLUGIN_PDF_DISPLAY_TYPE_CHOICES', display_type_choices)
