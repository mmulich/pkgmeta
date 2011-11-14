# -*- coding: utf-8 -*-
import os
from tempfile import mkdtemp
from packaging.metadata import Metadata

__all__ = (
    'METADATA_FILENAME',
    'make_metadata', 'populate_repo',
    )

METADATA_FILENAME = 'METADATA'


def make_metadata(common, versions, extended={}, cls=Metadata):
    mapping = common.copy()
    items = []
    for version in versions:
        mapping['version'] = version
        if version in extended:
            mapping.update(extended[version])
        items.append(cls(mapping=mapping))
    return items


def populate_repo(inhabitants, root=None):
    converted_inhabitants = []
    for i in inhabitants:
        converted_inhabitants.extend(make_metadata(*i))
    if root is None:
        root = mkdtemp()
    for metadata in converted_inhabitants:
        name = metadata['Name']
        version = metadata['Version']
        #: Write the file out to the filesystem under the
        #  <name>/<version>/METADATA file scheme
        dist_metadata_root = os.path.join(root, name)
        if not os.path.exists(dist_metadata_root):
            os.mkdir(dist_metadata_root)
        dest = os.path.join(root, name, version)
        filename = os.path.join(dest, METADATA_FILENAME)
        os.mkdir(dest)
        #: Write out the metadata file
        metadata.write(filename)
    return root
