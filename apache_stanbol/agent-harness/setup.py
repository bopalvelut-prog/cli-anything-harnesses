from setuptools import setup
setup(
    name='cli-anything-apache_stanbol',
    version='1.0.0',
    packages=['cli_anything.apache_stanbol'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_stanbol=cli_anything.apache_stanbol:cli']},
)
