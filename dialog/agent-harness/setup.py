from setuptools import setup
setup(
    name='cli-anything-dialog',
    version='1.0.0',
    packages=['cli_anything.dialog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dialog=cli_anything.dialog:cli']},
)
