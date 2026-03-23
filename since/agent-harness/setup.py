from setuptools import setup
setup(
    name='cli-anything-since',
    version='1.0.0',
    packages=['cli_anything.since'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-since=cli_anything.since:cli']},
)
