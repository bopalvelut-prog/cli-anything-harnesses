from setuptools import setup
setup(
    name='cli-anything-apache_knox',
    version='1.0.0',
    packages=['cli_anything.apache_knox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_knox=cli_anything.apache_knox:cli']},
)
