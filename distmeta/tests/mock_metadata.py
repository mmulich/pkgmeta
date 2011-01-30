# -*- coding: utf-8 -*-
ALL_DISTS = []

# Examples are a three value tuple:
# __1__   ({'name': "name", ...},
# __2__    (version, ...),
# __3__    {"version": {'description': "special description", ...},
#          )
#
# 1) Common metadata properties (e.g. name, description, etc.)
# 2) Versions to create in increasing order
# 3) An optional dictionary containing extra metadata keyed by version (e.g.
#    requires, provides, etc.)


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

soapbubble__versions = ('4.0', '5.0', '5.1', '5.2', '5.3', '6.0', '6.1')
soapbubble__extends = dict([(v, dict(provides_dist=['soapbar (>=%s)' % v]),)
                                for v in soapbubble__versions])
SOAPBUBBLE = ({'name': 'soapbubble',
               'description': "A lightweight SOAP library in pure Python",
               'author': "Scrubbing Bubble and Rubber Ducky",
               },
              soapbubble__versions,
              soapbubble__extends,
              )
ALL_DISTS.append(SOAPBUBBLE)

SANDBOX = ({'name': 'sandbox',
            'description': "A prototyping database that has the " \
                           "UniversalDB API",
            'author': "Baby Goob",
            },
           ('1.0', '2.0', '3.0', '4.0'),
           )
ALL_DISTS.append(SANDBOX)

waterweb_5_0__extends = dict(provides_dist=['earthweb (>=2.0)'])
WATERWEB = ({'name': 'waterweb',
             'description': "A water based web framework",
             'author': "Fireman John",
             },
            ('2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0'),
            {'5.0': waterweb_5_0__extends,
             '6.0': waterweb_5_0__extends,
             '7.0': waterweb_5_0__extends,
             #: 8.0 conflicts with fireweb, but we lack a metadata expression
             #  that can say a distribution conflicts with another.
             '8.0': dict(provides_dist=['earthweb (>=3.0)'],
                         ##obsoletes_dist='fireweb',
                         ),
             },
            )
ALL_DISTS.append(WATERWEB)

EARTHWEB = ({'name': 'earthweb',
             'description': "An earth based web framework",
             'author': "Joe Dirt",
             },
            ('1.0', '2.0', '3.0'),
            )
ALL_DISTS.append(EARTHWEB)

FIREWEB = ({'name': 'fireweb',
            'description': "A fire based web framework to burn all others",
            'author': "Logi",
            'provides_dist': ['waterweb (>=7.0,<8.0)',
                              #: Wouldn't it be nice to say provides soap?
                              'soapbar (>=6.1)',
                              'soapbubble (>=6.0)',
                              'earthweb (>=2.0)',
                              ],
            'obsoletes_dist': ['earthweb (>=2.0)'],
            },
           ('1.0',),
           )
ALL_DISTS.append(FIREWEB)

BIGBOX = ({'name': 'bigbox',
           'description': "A big box for all kinds of data",
           'author': "Roogle",
           'provides_dist': ['sandbox (>=4.0,<5.0)'],
           'obsoletes_dist': ['sandbox (>=4.0,<5.0)'],
           },
          ('1.0',),
          )
ALL_DISTS.append(BIGBOX)

WEBCAL = ({'name': 'webcal',
           'description': "Web calendaring application",
           'author': "Hathor",
           },
          ('1.0', '2.0', '3.0',),
          # TODO: Change soapbar to soapbubble, because it's the prototyping
          #       library in this scenario.
          {'1.0': dict(requires_dist=['solarcal',
                                      'sandbox (>=3.0)',
                                      'waterweb (>=5.0)',
                                      'soapbar (>=4.0)',
                                      ]),
           '2.0': dict(requires_dist=['solarcal',
                                      #: Provided by bigbox
                                      'sandbox (>=4.0)',
                                      'waterweb (>=7.0)',
                                      'soapbar (>=5.0.3,<6.0)',
                                      ]),
           '3.0': dict(requires_dist=['solarcal',
                                      'sandbox (>=4.0)',
                                      #: Both provided by fireweb
                                      'waterweb (>=8.0)',
                                      'soapbar (>=6.1)',
                                      ]),
           }
          )
ALL_DISTS.append(WEBCAL)
