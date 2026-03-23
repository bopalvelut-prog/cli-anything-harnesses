from setuptools import setup
setup(
    name='cli-anything-omnibus',
    version='1.0.0',
    packages=['cli_anything.omnibus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-omnibus=cli_anything.omnibus:cli']},
)
