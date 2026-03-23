from setuptools import setup
setup(
    name='cli-anything-apache_manifoldcf',
    version='1.0.0',
    packages=['cli_anything.apache_manifoldcf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_manifoldcf=cli_anything.apache_manifoldcf:cli']},
)
