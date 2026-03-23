from setuptools import setup
setup(
    name='cli-anything-apache_storm',
    version='1.0.0',
    packages=['cli_anything.apache_storm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_storm=cli_anything.apache_storm:cli']},
)
