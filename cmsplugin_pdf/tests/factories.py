"""Factories for the models of the ``cmsplugin_pdf`` app."""
import factory
from filer.models.filemodels import File

from ..models import PDFPluginModel


class FilerFileFactory(factory.DjangoModelFactory):
    """Factory for ``File`` objects of the django-filer app."""
    FACTORY_FOR = File

    owner = None
    original_filename = 'foobar.pdf'
    file = None


class PDFPluginModelFactory(factory.DjangoModelFactory):
    """Factory for the ``PDFPluginModel`` model."""
    FACTORY_FOR = PDFPluginModel

    file = factory.SubFactory(FilerFileFactory)
