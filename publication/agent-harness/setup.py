from setuptools import setup
setup(
    name='cli-anything-publication',
    version='1.0.0',
    packages=['cli_anything.publication'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-publication=cli_anything.publication:cli']},
)
