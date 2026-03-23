from setuptools import setup
setup(
    name='cli-anything-apache_jmeter',
    version='1.0.0',
    packages=['cli_anything.apache_jmeter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_jmeter=cli_anything.apache_jmeter:cli']},
)
