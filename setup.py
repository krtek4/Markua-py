#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="Markua",
    packages=find_packages(exclude=['tests']),
    version="0.0.1",
    license="WTFPL",
    description="Python parser for the Markua spec",
    author="Gilles Crettenand <gilles@crettenand.info>",
    author_email="gilles@crettenand.info",
    maintainer="Gilles Crettenand <gilles@crettenand.info>",
    maintainer_email="gilles@crettenand.info",
    url="https://github.com/krtek4/Markua-py",
    keywords=["markup", "markdown", "commonmark", "markua"],
    entry_points={
        'console_scripts': [
            'markua = Markua.markua:main',
        ]
    },
    install_requires=[
        'future',
        'commonmark'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities"])
