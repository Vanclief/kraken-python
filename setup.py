# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='krakenpy',
    version='0.1.0',
    description='Unofficial Python3 library for the Kraken API',
    long_description=readme,
    author='Franco Valencia',
    author_email='franco.avalencia@gmail.com',
    url='https://github.com/Vanclief/kraken-python',
    license=license,
    packages=find_packages(exclude=('tests'))
)
