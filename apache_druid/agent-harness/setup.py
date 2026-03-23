from setuptools import setup
setup(
    name='cli-anything-apache_druid',
    version='1.0.0',
    packages=['cli_anything.apache_druid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_druid=cli_anything.apache_druid:cli']},
)
