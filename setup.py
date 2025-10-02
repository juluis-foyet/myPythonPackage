from setuptools import setup, find_packages

setup(
    name='myPythonPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This is my first python package',
    long_description=open('README.md').read(),
    install_requires = ['numpy'],
    url='https://github.com/juluis-foyet/myPythonPackage.git',
    author='Juluis Foyet',
    author_email='visnelfoyet@gmail.com'
)