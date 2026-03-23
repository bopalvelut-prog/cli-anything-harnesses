from setuptools import setup
setup(
    name='cli-anything-apache_hbase',
    version='1.0.0',
    packages=['cli_anything.apache_hbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_hbase=cli_anything.apache_hbase:cli']},
)
