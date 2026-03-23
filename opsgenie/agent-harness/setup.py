from setuptools import setup
setup(
    name='cli-anything-opsgenie',
    version='1.0.0',
    packages=['cli_anything.opsgenie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opsgenie=cli_anything.opsgenie:cli']},
)
