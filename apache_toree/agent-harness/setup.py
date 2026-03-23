from setuptools import setup
setup(
    name='cli-anything-apache_toree',
    version='1.0.0',
    packages=['cli_anything.apache_toree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_toree=cli_anything.apache_toree:cli']},
)
