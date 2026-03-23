from setuptools import setup
setup(
    name='cli-anything-apache_pinot',
    version='1.0.0',
    packages=['cli_anything.apache_pinot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_pinot=cli_anything.apache_pinot:cli']},
)
