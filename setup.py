from setuptools import setup

setup(name='XmlStudioCleaner',
      version='1.0.2',
      packages=[
          'studio_cleaner'
      ],
      package_dir={'studio_cleaner':'src/studio_cleaner'},
      install_requires=[
          'PyRSS2Gen',
          'gdata',
          'youtube-dl'],
      entry_points={
          'console_scripts': [
              'xmlstudioclean = clean_studio_xml:main',
          ],
      })
