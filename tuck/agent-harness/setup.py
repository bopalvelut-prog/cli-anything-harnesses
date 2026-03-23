from setuptools import setup
setup(
    name='cli-anything-tuck',
    version='1.0.0',
    packages=['cli_anything.tuck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tuck=cli_anything.tuck:cli']},
)
