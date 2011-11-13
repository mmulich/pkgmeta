Package Metadata (pkgmeta)
==========================

A Python package used to create, read and update a Python metadata
repository. A metadata repository is a collection of Python
package (or distribution)
releases containing information about the package (metadata)
and where it can be found.
This information can then be used to find distributions
and their dependencies without actually acquiring (downloading) the
distribution itself.

The repository does not actually hold any distribution data. That type of
information can be found via more established means, such as
`PyPI <http://pypi.pythong.org/pypi/>`_. Furthermore, the repository can
and in most cases will use
the Python Package Index (see also
`PEP 301 <http://www.python.org/dev/peps/pep-0301/>`_)
standard for distribution source storage.
This should then allow for both the older
distutils and setuptools based code
to work happily with the repository scenario.

The repository holds information in Metadata 1.2 (:pep:`345`) format.
This package also provides a means
to convert lesser Metadata formats
to Metadata 1.2.
We are using Metadata 1.2,
because it is the standard that Python >= 3.3 will use.

The documentation has two major sections::

#. End-user usage and information
#. Administrative and developer usage

Contents:

.. toctree::
   :maxdepth: 2

   config
   tests

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

