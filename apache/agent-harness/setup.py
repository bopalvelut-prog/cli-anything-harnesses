from setuptools import setup
setup(
    name='cli-anything-apache',
    version='1.0.0',
    packages=['cli_anything.apache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache=cli_anything.apache:cli']},
)
