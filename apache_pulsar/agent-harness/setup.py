from setuptools import setup
setup(
    name='cli-anything-apache_pulsar',
    version='1.0.0',
    packages=['cli_anything.apache_pulsar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_pulsar=cli_anything.apache_pulsar:cli']},
)
