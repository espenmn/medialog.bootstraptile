from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='medialog.bootstraptile',
      version=version,
      description="Richtext tile for collective.cover to be used with bootstrap themes",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='collective cover bootstrap rich text',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='https://github.com/espenmn/medialog.bootstraptile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.cover' ,
          'zope.i18nmessageid',
          'plone.api',
      ],
      entry_points="""
      # -*- Entry points: -*-
    
        
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )


