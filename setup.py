from setuptools import setup, find_packages

setup(name='XmlStudioCleaner',
      version='1.0.2',
      packages=find_packages(),
      install_requires=[
          'PyRSS2Gen',
          'gdata',
          'youtube-dl'],
      entry_points={
          'console_scripts': [
              'xmlstudioclean = src.clean_studio_xml:main',
          ],
      })

