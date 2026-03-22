from setuptools import setup
setup(
    name='cli-anything-filerun',
    version='1.0.0',
    packages=['cli_anything.filerun'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-filerun=cli_anything.filerun:cli']},
)
