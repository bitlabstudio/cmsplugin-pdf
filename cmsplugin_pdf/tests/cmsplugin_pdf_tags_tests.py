"""Tests for the templatetags of the cmsplugin_pdf app."""
from django.test import TestCase

from ..templatetags.cmsplugin_pdf_tags import get_page_count
from .factories import PDFPluginModelFactory


class GetPageCountTestCase(TestCase):
    """Tests for the ``get_page_count`` template filter."""
    longMessage = True

    def test_filter(self):
        plugin = PDFPluginModelFactory()
        result = get_page_count(plugin.file.path)
        self.assertEqual(result, 1, msg=(
            'Should return the number of pages for the given file path'))
