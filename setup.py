#!/usr/bin/env python
from setuptools import setup

setup(
    name='meteogram-py',
    version='0.0.1',
    package_data={'': ['README.md']},
    packages=['meteogrampy'],

    # metadata for upload to PyPI
    author='Weather Decision Technologies',
    author_email='pkamis@wdtinc.com',
    description='Python module built around Matplotlib for quickly creating meteograms from weather data.',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
