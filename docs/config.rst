Configuration (pkgmeta.cfg)
===========================

In order to setup a repository, one needs to configure
one or more repositories using a basic INI file.

The configuration is fairly simple.
There is one INI section that is special,
it is called ``pkgmeta``. This section is used to configure global settings.
Any other sections in the file are repository definitions.

Example configuration
---------------------

The following configuration sets up a repository, named ``myrepo``,
and selects it as the default repository.
The ``myrepo`` repository is using the filesystem storage type
and sources from ``pkgmeta.org``.
::

    [pkgmeta]
    default = myrepo

    [myrepo]
    type = filesystem
    sources =
        http://repo.pkgmeta.org/ pypi
	http://repo.pkgmeta.org/ private

.. todo:: Currently, the sources implementation is not complete. Stay tuned for
   more information.
