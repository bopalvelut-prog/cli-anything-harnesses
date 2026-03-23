from setuptools import setup
setup(
    name='cli-anything-log',
    version='1.0.0',
    packages=['cli_anything.log'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-log=cli_anything.log:cli']},
)
