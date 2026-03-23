from setuptools import setup
setup(
    name='cli-anything-canonical',
    version='1.0.0',
    packages=['cli_anything.canonical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-canonical=cli_anything.canonical:cli']},
)
