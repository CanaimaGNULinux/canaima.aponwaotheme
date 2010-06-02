# -*- coding: utf-8 -*-
"""
Éste módulo contiene la herramienta de configuración del tema Canaima Aponwao
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()



setup(name='canaima.aponwaotheme',
      version='0.9',
      description="Versión instalable del tema Canaima Aponwao",
      long_description=open(os.path.join("docs", "README")).read() + "\n" +
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
      author_email='desarrolladores@canaima.softwarelibre.gob.ve',
      url='http://canaima.softwarelibre.gob.ve/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaima', 'canaima.aponwaotheme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools'],
      setup_requires = ["setuptools",],
      theme_vars = {
          'skinname'          : 'Tema Canaima Aponwao para Plone',
          'skinbase'          : 'Plone Default',
          'namespace_package' : 'canaima',
          'package'           : 'aponwaotheme',
          'used_subtemplates' : '',
      },
      )
