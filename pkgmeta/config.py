# -*- coding: utf-8 -*-
import os
import sysconfig
from pkgmeta.exceptions import ConfigNotFound

__all__ = (,)

_sysconfig_vars = sysconfig.get_config_vars()
PKG_HOME = os.path.dirname(__file__)
BASE_CONFIG = os.path.join(PKG_HOME, 'base_config')
SOURCE_LIST_LOCATIONS = os.path.join(BASE_CONFIG, 'source.list-locations')
PKGMETA_CFG_LOCATIONS = os.path.join(BASE_CONFIG, 'pkgmeta.cfg-locations')

# There are multiple locations where source.list[.d] configs can be found.
with open(SOURCE_LIST_LOCATIONS, 'r') as locations:
    # Note: Tuple comprehension won't work here, because it makes a generator.
    _sources = [loc.strip().format(pkgmeta_home=PKG_HOME,
                                   **_sysconfig_vars)
                for loc in locations.read().split('\n')
                if loc.strip() and not loc.strip().startswith('#')]
SOURCES = tuple(_sources)

# There are multiple locations where pkgmeta.cfg configs can be found.
with open(PKGMETA_CFG_LOCATIONS, 'r') as locations:
    # Note: Tuple comprehension won't work here, because it makes a generator.
    _cfgs = [loc.strip().format(pkgmeta_home=PKG_HOME,
                                   **_sysconfig_vars)
                for loc in locations.read().split('\n')
                if loc.strip() and not loc.strip().startswith('#')]
PKGMETA_CFGS = tuple(_cfgs)
