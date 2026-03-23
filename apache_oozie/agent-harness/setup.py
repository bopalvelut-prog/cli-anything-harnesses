from setuptools import setup
setup(
    name='cli-anything-apache_oozie',
    version='1.0.0',
    packages=['cli_anything.apache_oozie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_oozie=cli_anything.apache_oozie:cli']},
)
