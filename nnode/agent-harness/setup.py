from setuptools import setup
setup(
    name='cli-anything-nnode',
    version='1.0.0',
    packages=['cli_anything.nnode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nnode=cli_anything.nnode:cli']},
)
