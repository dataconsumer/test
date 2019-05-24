from distutils.core import setup
from setuptools import find_packages

setup(name='piptest',
version='1.0',
author='N Liu',
author_email='lldde@gmail.com',
url='https://github.com/dataconsumer/piptest',
packages=find_packages(),
install_requires=[
        "gensim >= 3.7.1"
    ]
)