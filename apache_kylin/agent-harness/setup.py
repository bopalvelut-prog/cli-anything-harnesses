from setuptools import setup
setup(
    name='cli-anything-apache_kylin',
    version='1.0.0',
    packages=['cli_anything.apache_kylin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_kylin=cli_anything.apache_kylin:cli']},
)
