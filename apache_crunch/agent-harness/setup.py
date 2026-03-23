from setuptools import setup
setup(
    name='cli-anything-apache_crunch',
    version='1.0.0',
    packages=['cli_anything.apache_crunch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_crunch=cli_anything.apache_crunch:cli']},
)
