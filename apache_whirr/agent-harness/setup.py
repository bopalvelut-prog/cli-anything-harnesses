from setuptools import setup
setup(
    name='cli-anything-apache_whirr',
    version='1.0.0',
    packages=['cli_anything.apache_whirr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_whirr=cli_anything.apache_whirr:cli']},
)
