#
# Snagged from CPython at revison 0feb5a5dbaeb
# https://bitbucket.org/mirror/cpython/raw/0feb5a5dbaeb/Lib/packaging/__init__.py
#
"""Support for packaging, distribution and installation of Python projects.

Third-party tools can use parts of packaging as building blocks
without causing the other modules to be imported:

    import packaging.version
    import packaging.metadata
    import packaging.pypi.simple
    import packaging.tests.pypi_server
"""

from logging import getLogger

__all__ = ['__version__', 'logger']

__version__ = "1.0a3"
logger = getLogger('packaging')
