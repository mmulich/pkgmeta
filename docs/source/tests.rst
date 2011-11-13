Testing
=======

Running the tests
-----------------

To test the package, use unittest test discovery::

    $ python -m unittest discover

Or for those of you using Python <= 2.6, you'll need to install unittest2
first. Then run the ``unit2`` script::

    $ pip install unittest2
    $ unit2 discover

Coverage reports
----------------

Calling python within coverage's run command doesn't work because of the ``-m`` option flag given to python. So you'll need to
create a script similar to unittest2's ``unit2``.

I created a script called ``testrunner.py`` and placed it outside the package, because you'll receive import errors if you put it along side the package you are trying to discover. The scripts contents are::

    # -*- coding: utf-8 -*-
    """Unittest test runner script"""

    __unittest = True

    from unittest.main import main, TestProgram, USAGE_AS_MAIN
    TestProgram.USAGE = USAGE_AS_MAIN

    main(module=None)

.. seealso:: `Integrating Coverage with Unittest Discovery <http://blog.wearpants.org/integrating-coverage-and-unittest-discovery/>`_

Now you can call coverage like so::

    $ coverage run --omit=~/testrunner.py ~/testrunner.py
