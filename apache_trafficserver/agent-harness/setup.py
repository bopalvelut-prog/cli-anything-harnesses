from setuptools import setup
setup(
    name='cli-anything-apache_trafficserver',
    version='1.0.0',
    packages=['cli_anything.apache_trafficserver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_trafficserver=cli_anything.apache_trafficserver:cli']},
)
