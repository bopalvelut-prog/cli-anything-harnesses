from setuptools import setup
setup(
    name='cli-anything-truffle',
    version='1.0.0',
    packages=['cli_anything.truffle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-truffle=cli_anything.truffle:cli']},
)
