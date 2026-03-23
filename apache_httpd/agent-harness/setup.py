from setuptools import setup
setup(
    name='cli-anything-apache_httpd',
    version='1.0.0',
    packages=['cli_anything.apache_httpd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_httpd=cli_anything.apache_httpd:cli']},
)
