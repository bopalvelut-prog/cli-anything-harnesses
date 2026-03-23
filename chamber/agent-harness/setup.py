from setuptools import setup
setup(
    name='cli-anything-chamber',
    version='1.0.0',
    packages=['cli_anything.chamber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chamber=cli_anything.chamber:cli']},
)
