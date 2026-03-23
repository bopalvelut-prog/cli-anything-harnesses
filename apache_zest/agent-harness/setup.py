from setuptools import setup
setup(
    name='cli-anything-apache_zest',
    version='1.0.0',
    packages=['cli_anything.apache_zest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_zest=cli_anything.apache_zest:cli']},
)
