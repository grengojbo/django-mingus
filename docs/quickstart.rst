.. _quickstart:

Quick Start
===========

This quick start assumes basic familiarity with `virtualenv <http://virtualenv.openplans.org/>`_, `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_, and `pip <http://pip.openplans.org/>`_. It also assumes you have `subversion <http://subversion.tigris.org/>`_, `mercurial <http://mercurial.selenic.com/>`_ and `git <http://git-scm.com/>`_ clients installed.

Create a virtual environment::

    mkvirtualenv myblog --no-site-packages
    workon myblog

Clone the django-mingus repository::

    git clone git://github.com/montylounge/django-mingus.git
    cd django-mingus/mingus/

Install the required apps::

    pip install -r stable-requirements.txt

Perform some project setup tasks::

    mv local_settings.py.template local_settings.py
    ./manage.py syncdb
    ./manage.py loaddata test_data.json
    ./manage.py runserver

Congratulations! You can now view the blog by visiting http://localhost:8000/. Once you've had a chance to poke around, you'll likely want to move on to :ref:`customization <customization>`.
