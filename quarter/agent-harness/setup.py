from setuptools import setup
setup(
    name='cli-anything-quarter',
    version='1.0.0',
    packages=['cli_anything.quarter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quarter=cli_anything.quarter:cli']},
)
