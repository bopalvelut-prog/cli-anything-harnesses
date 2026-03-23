from setuptools import setup
setup(
    name='cli-anything-apache_camel',
    version='1.0.0',
    packages=['cli_anything.apache_camel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_camel=cli_anything.apache_camel:cli']},
)
