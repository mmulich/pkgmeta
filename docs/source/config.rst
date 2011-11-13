Configuration (pkgmeta.cfg)
===========================

In order to setup a repository, one needs to configure using a basic INI file.

The configuration fairly simple. There is one INI section that is special,
it is called ``pkgmeta``. This section is used to configure ``pkgmeta``
itself. Any other sections in the file are repository definitions.

Configuration example
---------------------

::

    [pkgmeta]
    default = myrepo

    [myrepo]
    sources =
        http://repo.pkgmeta.org/ pypi
	http://repo.pkgmeta.org/ private
