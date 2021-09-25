from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
  name = 'run-js',
  packages = ['js'],
  include_package_data=True,
  package_data = {'': ['*.js']},
  version = '0.0.0',
  description = 'Goal: The Easiest Way to Run JavaScript in Python',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/run-js',
  download_url = 'https://github.com/DanielJDufour/run-js/tarball/download',
  keywords = ['functional', 'javascript', 'python', 'package', 'library', 'universal', 'python3'],
  classifiers = [
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
  install_requires=[]
