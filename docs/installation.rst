.. _installation:

Installation
============

Installation assumes basic familiarity with `virtualenv`_, `virtualenvwrapper`_, and `pip`_. It also assumes you have `subversion`_, `mercurial`_ and `git`_ clients installed.

Set up environment
------------------

Create a virtual environment::

    mkvirtualenv myblog --no-site-packages
    workon myblog

Install requirements
--------------------

Install the required apps::

    pip install -r http://github.com/montylounge/django-mingus/blob/0.9.7/mingus/stable-requirements.txt?raw=true

Install Django-Mingus. You can install from PyPI::

    pip install django-mingus==0.9.7

Or directly from the source code on Github::

    pip install -e git+git://github.com/montylounge/django-mingus.git@0.9.7#egg=django-mingus

Set up Django project
---------------------

Create a new Django project (or use your existing project)::

    django-admin.py startproject myblog
    cd myblog

Customize settings.py
---------------------

Determine which applications you would like to use and add them to your INSTALLED_APPS. See :ref:`deciding` for more info.

To gain access to all of the features of all of the applications, an example project is included in the source with a `settings.py` file containing the following::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.sitemaps',
        'django.contrib.flatpages',
        'django.contrib.redirects',

        'django_extensions',
        'tagging',
        'djangodblog',
        'disqus',
        'basic.inlines',
        'basic.blog',
        'basic.bookmarks',
        'basic.media',
        'oembed',
        'flatblocks',
        'dbtemplates',
        'navbar',
        'sorl.thumbnail',
        'template_utils',
        'django_proxy',

        'django_markup',
        'google_analytics',
        'robots',
        'basic.elsewhere',
        'compressor',
        'contact_form',
        'honeypot',
        'sugar',
        'quoteme',
        'mingus.core',
        'debug_toolbar',

        'django_twitter',
        'django_bitly',
        'staticfiles',
        'tinymce',
        'django_wysiwyg',
        'cropper',
        'memcache_status',
        'request',
    )

**NOTE**: Many of the applications used by Django-Mingus have their own custom settings available. Take a look at the settings.py and local_settings.py.template files included with the Django-Mingus source files to get an idea of some typical settings. You should consult each application's documentation for more detailed information.

Sync and run
------------

Synchronize your database and fire up a local server::

    ./manage.py syncdb
    ./manage.py runserver

Next steps
----------

Congratulations! You can now view the blog by visiting http://localhost:8000/. Once you've had a chance to poke around, you'll likely want to move on to :ref:`customization <customization>`.

.. _virtualenv: http://virtualenv.openplans.org/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
.. _pip: http://pip.openplans.org/
.. _subversion: http://subversion.tigris.org/
.. _mercurial: http://mercurial.selenic.com/
.. _git: http://git-scm.com/
