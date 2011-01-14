# -*- coding: utf-8 -*-
import os
from tempfile import mkdtemp
from distutils2.metadata import DistributionMetadata


METADATA_FILENAME = 'METADATA'
ALL_DISTS = []


def _make_metadata(common, extended={}):
    md = dict(common)
    md.update(extended)
    return DistributionMetadata(mapping=md)


SOLARCAL = (_make_metadata({'name': 'solarcal',
                            'version': '1.0',
                            'summary': "Calendar based on solar dates.",
                            'author': "Ra",
                            }),
            )
ALL_DISTS.extend(SOLARCAL)

common = {'name': 'soapbar',
          'description': "Optimized SOAP library.",
          'author': "Rubber Ducky",
          }
SOAPBAR = (_make_metadata(common, {'version': '4.0'}),
           _make_metadata(common, {'version': '4.0.1'}),
           _make_metadata(common, {'version': '4.1'}),
           _make_metadata(common, {'version': '5.0.1'}),
           _make_metadata(common, {'version': '5.1'}),
           _make_metadata(common, {'version': '5.2'}),
           _make_metadata(common, {'version': '5.2.1'}),
           _make_metadata(common, {'version': '5.3'}),
           _make_metadata(common, {'version': '6.0'}),
           _make_metadata(common, {'version': '6.0.1'}),
           _make_metadata(common, {'version': '6.0.2'}),
           _make_metadata(common, {'version': '6.1'},)
           )
ALL_DISTS.extend(SOAPBAR)

def populate_repo(inhabitants, root=None):
    if root is None:
        root = mkdtemp()
    for metadata in inhabitants:
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
