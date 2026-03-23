from setuptools import setup
setup(
    name='cli-anything-apache_eagle',
    version='1.0.0',
    packages=['cli_anything.apache_eagle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_eagle=cli_anything.apache_eagle:cli']},
)
