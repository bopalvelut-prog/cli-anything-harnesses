from setuptools import setup
setup(
    name='cli-anything-apache_carbondata',
    version='1.0.0',
    packages=['cli_anything.apache_carbondata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_carbondata=cli_anything.apache_carbondata:cli']},
)
