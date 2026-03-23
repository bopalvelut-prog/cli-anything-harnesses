from setuptools import setup
setup(
    name='cli-anything-apache_mesos',
    version='1.0.0',
    packages=['cli_anything.apache_mesos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_mesos=cli_anything.apache_mesos:cli']},
)
