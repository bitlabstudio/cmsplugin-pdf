"""Templatetags for the cmsplugin_pdf app."""
from django import template

from pyPdf import PdfFileReader


register = template.Library()


@register.filter
def get_page_count(pdf_file_path):
    """
    Returns the number of pages of a given pdf file.

    Usage::

        {% load cmsplugin_pdf_tags %}
        Pages: {{ pdf_plugin.file.path|get_page_count }}

    """
    pdf = PdfFileReader(file(pdf_file_path, "rb"))
    return pdf.getNumPages()
