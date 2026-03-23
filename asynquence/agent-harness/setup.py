from setuptools import setup
setup(
    name='cli-anything-asynquence',
    version='1.0.0',
    packages=['cli_anything.asynquence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asynquence=cli_anything.asynquence:cli']},
)
