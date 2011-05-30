Package Metadata (pkgmeta)
==========================

A Python package used to create, read and update a Python metadata
repository. A metadata repository is a collection of Python
package or distribution
releases containing information about the package (a.k.a. metadata) and
where it can be found. This information can then be used to find distributions
and their dependencies without actually acquiring (downloading) the
distribution itself.

The repository does not actually hold any distribution data. That type of
information can be found via more established means, such as `PyPI
<http://pypi.pythong.org/pypi/>`_.

The repository holds information in Metadata 1.2 (:pep:`345`) format.
To prevent a lot of pain and tears,
lesser Metadata formats can be transitioned to Metadata 1.2.

The documentation has two major sections::

#. End-user usage and information
#. Administrative and developer usage

Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

