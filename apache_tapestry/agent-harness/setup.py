from setuptools import setup
setup(
    name='cli-anything-apache_tapestry',
    version='1.0.0',
    packages=['cli_anything.apache_tapestry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_tapestry=cli_anything.apache_tapestry:cli']},
)
