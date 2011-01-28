.. distmeta documentation master file, created by
   sphinx-quickstart on Fri Jan 14 16:03:05 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

distmeta's documentation
========================

A Python distribution used to create, read and update a Python metadata
repository. A metadata repository is a collection of Python distribution
releases containing information about the distribution (a.k.a. metadata) and
where it can be found. This information can then be used to find distributions
and their dependencies without actually acquiring (e.g. downloading) the
distribution itself.

The repository does not actually hold any distribution data. That type of
information can be found via more established means, such as `PyPI
<http://pypi.pythong.org/pypi/>`_.

The repository holds information in Metadata 1.2 (:pep:`345`) format. This is
the native format used by `Distutils2
<http://pypi.python.org/pypi/Distutils2/>`_. With a lot of pain and tears,
lesser Metadata formats can be transitioned to Metadata 1.2.

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

