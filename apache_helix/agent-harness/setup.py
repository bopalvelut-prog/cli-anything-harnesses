from setuptools import setup
setup(
    name='cli-anything-apache_helix',
    version='1.0.0',
    packages=['cli_anything.apache_helix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_helix=cli_anything.apache_helix:cli']},
)
