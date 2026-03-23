from setuptools import setup
setup(
    name='cli-anything-ravendb',
    version='1.0.0',
    packages=['cli_anything.ravendb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ravendb=cli_anything.ravendb:cli']},
)
