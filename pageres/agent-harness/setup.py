from setuptools import setup
setup(
    name='cli-anything-pageres',
    version='1.0.0',
    packages=['cli_anything.pageres'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pageres=cli_anything.pageres:cli']},
)
