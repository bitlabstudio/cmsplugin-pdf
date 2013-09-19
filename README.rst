CMSplugin PDF
=============

A reusable Django app to add PDFs to Django-CMS.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install django-cms
    pip install django-filer
    pip install Pillow

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-pdf

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-pdf.git#egg=cmsplugin_pdf

Add ``cmsplugin_pdf`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_pdf',
    )


Usage
-----

Create a CMS page with a placeholder, upload a pdf file using filer and simply
insert the plugin ``PDF File``.


Note that currently the thumbnail size is adjusted only in the template at
``cmsplugin_pdf/partials/pdf.html``.


Templatetags
------------

get_page_count
++++++++++++++

Use this template filter if you would like to display the page count for a pdf
file::

    {% load cmsplugin_pdf_tags %}
    Pages: {{ pdf_plugin.file.path|get_page_count }}


Settings
--------

CMSPLUGIN_PDF_DISPLAY_TYPE_CHOICES
++++++++++++++++++++++++++++++++++

Default::

    [
        ('standard', _('standard')),
        ('small', _('small')),
        ('highlight', _('highlight')),
    ]

When using the ``PDF File`` plugin in your django-cms placeholders you will
notice that you have three choices for the ``Display type``. This field
can be helpful when you want to render a file differently in different parts
of your site. If you need even more display types, just set this setting to
a different list of tuples.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-pdf
    $ pip install -r test_requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
