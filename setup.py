#!/usr/bin/env python
import sys
from setuptools import setup

if sys.version_info < (3,4):
    sys.exit('Sorry, Python < 3.4 is not supported')

setup(
    name = 'rss2twitter',
    version = '0.0.4',
    package_dir = {'': 'src'},
    data_files = [('etc/rss2twitter', ['src/config-sample.ini'])],
    scripts = ['src/rss2twitter.py'],
    install_requires = ['feedparser', 'tweepy>=1.8'],

    long_description=open('README.txt').read(),
    author = 'Todd Eddy, MKody',
    author_email = 'vr@removethispart.vrillusions.com, gh@kdy.ch',
    description = 'Checks rss feed for new posts and adds them to twitter.',
    url = 'https://github.com/mkody/rss2twitter',
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        ],
)
