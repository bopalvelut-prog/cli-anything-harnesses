from setuptools import setup
setup(
    name='cli-anything-apache_ode',
    version='1.0.0',
    packages=['cli_anything.apache_ode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_ode=cli_anything.apache_ode:cli']},
)
