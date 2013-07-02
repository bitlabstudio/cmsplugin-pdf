"""CMS Plugins for the ``cmsplugin_pdf`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PDFPluginModel


class PDFPlugin(CMSPluginBase):
    model = PDFPluginModel
    name = _('PDF File')
    render_template = 'cmsplugin_pdf/partials/pdf.html'

    def render(self, context, instance, placeholder):
        context.update({'pdf_plugin': instance})
        return context

plugin_pool.register_plugin(PDFPlugin)
