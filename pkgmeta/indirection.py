# -*- coding: utf-8 -*-
"""\
A package used to give direction for backwards and forwards compatiblity.
"""
import sys
try:
    import packaging
except ImportError:
    # This indirection contains forwards compatibility for select
    # parts of packaging.
    from pkgmeta._compat import packaging
    sys.modules['packaging'] = packaging
