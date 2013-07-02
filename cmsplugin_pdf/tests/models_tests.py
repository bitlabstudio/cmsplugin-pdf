"""Tests for the models of the ``cmsplugin_pdf`` app."""
from django.test import TestCase

from .factories import PDFPluginModelFactory


class PDFPluginModelTestCase(TestCase):
    """Tests for the ``PDFPluginModel`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``PDFPluginModel`` model."""
        pdfpluginmodel = PDFPluginModelFactory()
        self.assertTrue(pdfpluginmodel.pk)
