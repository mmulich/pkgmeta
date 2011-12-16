Example
=======

Initializing the example
------------------------

.. note:: In order to work on this example you will need to either check out
   a copy of the source or download it from PyPI.

Along side the ``pkgmeta`` source package is an example directory
which contains an example configuration
and a small script to populate the repository with
fake distributions.

To initialize the example, change directories to the pkgmeta project root::

    $ cd [where ever pkgmeta is located]
    $ ls
    README.rst  docs        example     pkgmeta

Run the ``make.py`` script::

    $ python3.2 example/make.py
    Creating the repository directory:  ~/example-repo
    Populating repository with example data...
    Writing configuration:  example.cfg
    Reading configuration...
    Loaded 9 distributions into the repository
    --------------------------------------------------------------------------------
    You can now use the example data by supplying the pkgmeta script with the configuration file flag:  -c ~/example.cfg

.. note:: If you haven't installed pkgmeta into Python's site-packages directory,
   you'll need to add the sources location to the ``PYTHONPATH`` environment
   variable.

Walk through
------------

Now that we've created an example repository,
we can probe it for information.

A brief example might be
to search for distributions containing the term ``cal``::

    $ pkgmeta -c ~/example.cfg search cal
    p   solarcal          - Calendar based on solar dates.                          
    p   webcal            - Web calendaring application

.. note:: We passed in the example configuration with the ``-c`` option.
   This is necessary, because without it the pkgmeta script will try
   (and most likely fail) to find the main configuration file.

Now that we've found some distributions, let's try showing the distributions
metadata::

    $ pkgmeta -c ~/example.cfg show webcal
    Metadata-Version: 1.2
    Name: webcal
    Version: 3.0
    Summary: Web calendaring application
    Description: UNKNOWN
    Home-page: UNKNOWN
    Author: Hathor
    Author-email: UNKNOWN
    Maintainer: UNKNOWN
    Maintainer-email: UNKNOWN
    License: UNKNOWN
    Download-URL: UNKNOWN
    Requires-Dist: solarcal, sandbox (>=4.0), waterweb (>=8.0), soapbar (>=6.1)
    Requires-Python: UNKNOWN
