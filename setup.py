import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name = "TED Wrapper",
    version = "1.2.0",
    author = "FIS Infrastructure Team",
    author_email = "oa.it-infrastructure@austin.utexas.edu",
    description = ("Convenience wrapper for TED."),
    url = "https://github.com/UT-Austin-FIS/ted_wrapper/",
    packages = find_packages(),
    install_requires = ['simpleldap>=0.7.1'],
    extras_require = {
        'ted.django':  ["django>=1.0"],
        'tests': ["django>=1.4", "mock>=1.0.1", "nose", "unittest2"],
    },
    long_description = read("README.md"),
    classifiers=["Development Status :: 5 - Production/Stable"],
)
