from setuptools import setup
setup(
    name='cli-anything-telescope',
    version='1.0.0',
    packages=['cli_anything.telescope'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-telescope=cli_anything.telescope:cli']},
)
