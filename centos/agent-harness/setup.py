from setuptools import setup
setup(
    name='cli-anything-centos',
    version='1.0.0',
    packages=['cli_anything.centos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-centos=cli_anything.centos:cli']},
)
