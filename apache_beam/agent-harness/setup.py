from setuptools import setup
setup(
    name='cli-anything-apache_beam',
    version='1.0.0',
    packages=['cli_anything.apache_beam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_beam=cli_anything.apache_beam:cli']},
)
