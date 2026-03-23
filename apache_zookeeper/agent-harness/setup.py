from setuptools import setup
setup(
    name='cli-anything-apache_zookeeper',
    version='1.0.0',
    packages=['cli_anything.apache_zookeeper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_zookeeper=cli_anything.apache_zookeeper:cli']},
)
