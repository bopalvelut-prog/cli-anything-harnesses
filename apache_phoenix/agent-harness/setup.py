from setuptools import setup
setup(
    name='cli-anything-apache_phoenix',
    version='1.0.0',
    packages=['cli_anything.apache_phoenix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_phoenix=cli_anything.apache_phoenix:cli']},
)
