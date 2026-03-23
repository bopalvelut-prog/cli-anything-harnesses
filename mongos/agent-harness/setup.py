from setuptools import setup
setup(
    name='cli-anything-mongos',
    version='1.0.0',
    packages=['cli_anything.mongos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mongos=cli_anything.mongos:cli']},
)
