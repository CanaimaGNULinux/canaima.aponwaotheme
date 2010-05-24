# -*- coding: utf-8 -*-
"""
Éste módulo contiene la herramienta de configuración del tema Canaima Aponwao
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

tests_require=['zope.testing']

setup(name='canaima.aponwaotheme',
      version=version,
      description="Versión instalable del tema Canaima Aponwao",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone theme canaima gnu linux aponwao cms',
      author='Equipo de Desarrollo de Canaima GNU/Linux',
      author_email='canaima@canaima.softwarelibre.gob.ve',
      url='http://canaima.softwarelibre.gob.ve/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaima', 'canaima.aponwaotheme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'canaima.aponwaotheme.tests',
      entry_points="""
      # -*- entry_points -*- 
      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list
      theme_vars = distwriters:assert_dict

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      theme_vars.txt = distwriters:write_map

      """,
      paster_plugins = ["ZopeSkel",],
      setup_requires = ["setuptools",],
      theme_vars = {'skinname': 'Canaima Aponwao',
          'skinbase'          : 'Plone Default',
          'namespace_package' : 'canaima',
          'package'           : 'aponwaotheme',
          'used_subtemplates' : '',
      },
      )
