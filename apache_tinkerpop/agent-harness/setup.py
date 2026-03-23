from setuptools import setup
setup(
    name='cli-anything-apache_tinkerpop',
    version='1.0.0',
    packages=['cli_anything.apache_tinkerpop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_tinkerpop=cli_anything.apache_tinkerpop:cli']},
)
