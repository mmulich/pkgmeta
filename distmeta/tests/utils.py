# -*- coding: utf-8 -*-
import os
from tempfile import mkdtemp
from distutils2.metadata import DistributionMetadata


METADATA_FILENAME = 'METADATA'
ALL_DISTS = []


def _make_metadata(common, versions, extended={}):
    mapping = common.copy()
    items = []
    for version in versions:
        mapping['version'] = version
        if version in extended:
            mapping.update(extended[version])
        items.append(DistributionMetadata(mapping=mapping))
    return items


# Examples are a three value tuple:
# ({'name': "name", ...}, # (1)
#  (version, ...), # (2)
#  {"version": {'description': "special description", ...}, # (3)
#  )
#
# 1) Common metadata dictionary
# 2) Versions to create in increasing order
# 3) An optional dictionary containing extra metadata keyed by version


SOLARCAL = ({'name': 'solarcal',
             'version': '1.0',
             'summary': "Calendar based on solar dates.",
             'author': "Ra",
             },
            ('1.0',),
            )
ALL_DISTS.append(SOLARCAL)

SOAPBAR = ({'name': 'soapbar',
            'description': "Optimized SOAP library.",
            'author': "Rubber Ducky",
            },
           ('4.0dev', '4.0', '4.1a1', '4.1a2',
            '5.0a1', '5.0b1', '5.0', '5.0.1', '5.1', '5.2', '5.2.1', '5.3',
            '6.0', '6.1'),
           )
ALL_DISTS.append(SOAPBAR)

SHAMPOO = ({'name': 'shampoo',
            'description': "SOAP library tailored for use with the Hair API.",
            'author': "Shamu",
            },
           ('1.0',),
           {'1.0': dict(provides_dist=['soapbar (>=5.0)'])}
           )
ALL_DISTS.append(SHAMPOO)

def populate_repo(inhabitants, root=None):
    converted_inhabitants = []
    for i in inhabitants:
        converted_inhabitants.extend(_make_metadata(*i))
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
