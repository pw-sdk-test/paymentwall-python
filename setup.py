import os
#from distutils.core import setup
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='paymentwall-python',
    version='2.0.0',
    packages=['paymentwall'],
    install_requires=['certifi==2023.07.22'],
    url='https://github.com/pw-sdk-test/paymentwall-python',
    description='Paymentwall Python Library',
    long_description=read('pypi_description.rst'),
    license='MIT',
    author='Paymentwall Team',
    author_email='devsupport@paymentwall.com'
)
