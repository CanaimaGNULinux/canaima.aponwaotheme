# -*- coding: utf-8 -*-
"""
Éste módulo contiene la herramienta de configuración de la instalación del tema Canaima Aponwao
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='canaima.aponwaotheme',
      version='1.0',
      description='Tema Canaima Aponwao para Plone, basado en la Metadistribución venezolana "Canaima GNU/Linux"',
      long_description="\n\n" + open(os.path.join("docs", "README.txt")).read() + "\n\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone theme canaima gnu linux aponwao cms',
      author='Equipo de Desarrollo de Canaima GNU/Linux\n\t\t\tLuis Martínez\n\t\t\tLeonardo Caballero\n\t\t\tXavier Araque',
      author_email='desarrolladores@canaima.softwarelibre.gob.ve',
      url='http://canaima.softwarelibre.gob.ve/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaima', 'canaima.aponwaotheme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',],
      setup_requires=['setuptools',],
      theme_vars={
          'skinname'          : 'Canaima Aponwao',
          'skinbase'          : 'Plone Default',
          'namespace_package' : 'canaima',
          'package'           : 'aponwaotheme',
      },
      )