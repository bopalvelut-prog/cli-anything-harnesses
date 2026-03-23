from setuptools import setup
setup(
    name='cli-anything-apache_submarine',
    version='1.0.0',
    packages=['cli_anything.apache_submarine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_submarine=cli_anything.apache_submarine:cli']},
)
