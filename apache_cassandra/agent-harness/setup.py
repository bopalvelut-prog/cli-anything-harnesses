from setuptools import setup
setup(
    name='cli-anything-apache_cassandra',
    version='1.0.0',
    packages=['cli_anything.apache_cassandra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_cassandra=cli_anything.apache_cassandra:cli']},
)
