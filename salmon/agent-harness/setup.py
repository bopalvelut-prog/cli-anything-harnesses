from setuptools import setup
setup(
    name='cli-anything-salmon',
    version='1.0.0',
    packages=['cli_anything.salmon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salmon=cli_anything.salmon:cli']},
)
