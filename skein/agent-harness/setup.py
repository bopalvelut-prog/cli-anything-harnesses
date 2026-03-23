from setuptools import setup
setup(
    name='cli-anything-skein',
    version='1.0.0',
    packages=['cli_anything.skein'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skein=cli_anything.skein:cli']},
)
