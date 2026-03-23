from setuptools import setup
setup(
    name='cli-anything-gang',
    version='1.0.0',
    packages=['cli_anything.gang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gang=cli_anything.gang:cli']},
)
