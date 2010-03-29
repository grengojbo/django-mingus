.. _customization:

Customization
=============

.. _themes:

Themes
******

The default theme used by django-mingus is Basic. Django-Mingus also comes with 4 additional themes:

* Django(green)
* Minimal (black/white)
* Dark (black)
* JeffCroft (brown/pink)

You can `view screenshots <http://www.flickr.com/photos/37875916@N07/tags/mingustheme/>`_ of the themes on Flickr.

To switch themes just change this line in templates/base.html::

    <link rel="stylesheet" href="{{ STATIC_URL }}mingus/css/themes/basic.css" type="text/css" media="all" charset="utf-8">

For example, to use the Dark theme, you would change the code like so::

    <link rel="stylesheet" href="{{ STATIC_URL }}mingus/css/themes/dark.css" type="text/css" media="all" charset="utf-8">

Or you can create your own theme and point directly to that::

    <link rel="stylesheet" href="{{ STATIC_URL }}path/to/your.css" type="text/css" media="all" charset="utf-8">
