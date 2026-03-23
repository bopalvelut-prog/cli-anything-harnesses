from setuptools import setup
setup(
    name='cli-anything-atlassian_opsgenie',
    version='1.0.0',
    packages=['cli_anything.atlassian_opsgenie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlassian_opsgenie=cli_anything.atlassian_opsgenie:cli']},
)
