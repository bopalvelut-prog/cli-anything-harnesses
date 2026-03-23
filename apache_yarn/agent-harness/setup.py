from setuptools import setup
setup(
    name='cli-anything-apache_yarn',
    version='1.0.0',
    packages=['cli_anything.apache_yarn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_yarn=cli_anything.apache_yarn:cli']},
)
