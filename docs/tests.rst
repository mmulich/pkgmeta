Testing
=======

Running the tests
-----------------

To test the package, use unittest's test discovery by running the following
within pkgmeta's project root::

    $ python -m unittest discover

.. The following is for when Python < 3.2 is supported.

.. Or for those of you using Python <= 2.6, you'll need to install unittest2
   first. Then run the ``unit2`` script::

       $ pip install unittest2
       $ unit2 discover

Coverage reports
----------------

Calling Python within coverage's run command doesn't work
because of the ``-m`` option flag conflicts with the coverage command options.
In order to resolve the issue, a script similar to unittest2's ``unit2``
will need to be used.

Create a script called ``testrunner.py``
and placed it in your home directory.

.. note:: You can place the script anywhere outside the package root.
   If you put the script within the package, you will receive import errors
   when trying to do test discovery.

The scripts contents are::

    # -*- coding: utf-8 -*-
    """Unittest test runner script"""

    __unittest = True

    from unittest.main import main, TestProgram, USAGE_AS_MAIN
    TestProgram.USAGE = USAGE_AS_MAIN

    main(module=None)

.. seealso:: `Integrating Coverage with Unittest Discovery <http://blog.wearpants.org/integrating-coverage-and-unittest-discovery/>`_

Now call coverage like so::

    $ coverage run --omit=~/testrunner.py ~/testrunner.py
