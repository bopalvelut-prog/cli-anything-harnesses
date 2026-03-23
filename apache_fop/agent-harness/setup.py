from setuptools import setup
setup(
    name='cli-anything-apache_fop',
    version='1.0.0',
    packages=['cli_anything.apache_fop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_fop=cli_anything.apache_fop:cli']},
)
