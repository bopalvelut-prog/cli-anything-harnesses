from setuptools import setup
setup(
    name='cli-anything-newrelic',
    version='1.0.0',
    packages=['cli_anything.newrelic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-newrelic=cli_anything.newrelic:cli']},
)
