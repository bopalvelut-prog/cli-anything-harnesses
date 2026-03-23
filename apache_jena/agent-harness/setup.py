from setuptools import setup
setup(
    name='cli-anything-apache_jena',
    version='1.0.0',
    packages=['cli_anything.apache_jena'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_jena=cli_anything.apache_jena:cli']},
)
