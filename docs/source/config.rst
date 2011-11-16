Configuration (pkgmeta.cfg)
===========================

In order to setup a repository, one needs to configure using a basic INI file.

The configuration fairly simple. There is one INI section that is special,
it is called ``pkgmeta``. This section is used to configure globals.
Any other sections in the file are repository definitions.

Example configuration
---------------------

The following configuration selects the ``myrepo`` as the default repository. The ``myrepo`` repository using the filesystem storage type and sources from ``pkgmeta.org``.
::

    [pkgmeta]
    default = myrepo

    [myrepo]
    type = fs
    sources =
        http://repo.pkgmeta.org/ pypi
	http://repo.pkgmeta.org/ private
