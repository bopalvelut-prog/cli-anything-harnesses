from setuptools import setup
setup(
    name='cli-anything-paperform',
    version='1.0.0',
    packages=['cli_anything.paperform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paperform=cli_anything.paperform:cli']},
)
