from setuptools import setup
setup(
    name='cli-anything-virus',
    version='1.0.0',
    packages=['cli_anything.virus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-virus=cli_anything.virus:cli']},
)
