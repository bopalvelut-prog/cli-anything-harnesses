from setuptools import setup
setup(
    name='cli-anything-apache_groovy',
    version='1.0.0',
    packages=['cli_anything.apache_groovy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_groovy=cli_anything.apache_groovy:cli']},
)
