Testing
=======

Running the tests
-----------------

To test the package, use unittest test discovery, by running the following
within the pkgmeta's package root::

    $ python -m unittest discover

.. Or for those of you using Python <= 2.6, you'll need to install unittest2
   first. Then run the ``unit2`` script::

       $ pip install unittest2
       $ unit2 discover

Coverage reports
----------------

Calling python within coverage's run command doesn't work
because of the ``-m`` option flag given to python
conflicts with the coverage command options.
So you'll need to create a script similar to unittest2's ``unit2``.

To solve the fore mentioned issue, I created a script called ``testrunner.py``
and placed it in my home directory.
You can place the script anywhere outside the package root.
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

Now you can call coverage like so::

    $ coverage run --omit=~/testrunner.py ~/testrunner.py
