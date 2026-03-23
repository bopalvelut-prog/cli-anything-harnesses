from setuptools import setup
setup(
    name='cli-anything-apache_ant',
    version='1.0.0',
    packages=['cli_anything.apache_ant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_ant=cli_anything.apache_ant:cli']},
)
