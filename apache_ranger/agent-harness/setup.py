from setuptools import setup
setup(
    name='cli-anything-apache_ranger',
    version='1.0.0',
    packages=['cli_anything.apache_ranger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_ranger=cli_anything.apache_ranger:cli']},
)
