# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in raissyon/__init__.py
from raissyon import __version__ as version

setup(
	name='raissyon',
	version=version,
	description='Custom app for raissyon customization',
	author='Accurate Systems',
	author_email='info@accuratesystems.com.sa',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
