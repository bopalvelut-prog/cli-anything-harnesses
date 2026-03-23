from setuptools import setup
setup(
    name='cli-anything-openldap',
    version='1.0.0',
    packages=['cli_anything.openldap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openldap=cli_anything.openldap:cli']},
)
