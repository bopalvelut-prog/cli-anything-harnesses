from setuptools import setup
setup(
    name='cli-anything-apache_parquet',
    version='1.0.0',
    packages=['cli_anything.apache_parquet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_parquet=cli_anything.apache_parquet:cli']},
)
