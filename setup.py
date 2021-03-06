from setuptools import setup, find_packages

readme = open("README.txt").read().strip()
history = open("CHANGES.rst").read().strip()

setup(name='Products.feedfeeder',
      version='2.2.dev0',
      description="Turn external feed entries into content items",
      long_description= readme + "\n\n" + history,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='',
      author='Zest Software',
      author_email='m.van.rees@zestsoftware.nl',
      url='http://plone.org/products/feedfeeder',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'FeedParser',
          'BeautifulSoup',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
