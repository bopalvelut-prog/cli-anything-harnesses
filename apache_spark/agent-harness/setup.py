from setuptools import setup
setup(
    name='cli-anything-apache_spark',
    version='1.0.0',
    packages=['cli_anything.apache_spark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_spark=cli_anything.apache_spark:cli']},
)
