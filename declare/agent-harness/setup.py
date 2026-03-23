from setuptools import setup
setup(
    name='cli-anything-declare',
    version='1.0.0',
    packages=['cli_anything.declare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-declare=cli_anything.declare:cli']},
)
