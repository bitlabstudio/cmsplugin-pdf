"""Factories for the models of the ``cmsplugin_pdf`` app."""
import os

from django.conf import settings
from django.core.files import File as DjangoFile

import factory
from filer.models.filemodels import File

from ..models import PDFPluginModel


test_file = DjangoFile(open(os.path.join(settings.PROJECT_ROOT,
                       'tests/test_files/Lose away.pdf')))


class FilerFileFactory(factory.DjangoModelFactory):
    """Factory for ``File`` objects of the django-filer app."""
    FACTORY_FOR = File

    owner = None
    original_filename = 'foobar.pdf'
    # TODO needs some cleanup, since they don't auto-delete yet once the
    # model class is destroyed
    file = test_file


class PDFPluginModelFactory(factory.DjangoModelFactory):
    """Factory for the ``PDFPluginModel`` model."""
    FACTORY_FOR = PDFPluginModel

    file = factory.SubFactory(FilerFileFactory)
