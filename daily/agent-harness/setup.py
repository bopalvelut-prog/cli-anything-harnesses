from setuptools import setup
setup(
    name='cli-anything-daily',
    version='1.0.0',
    packages=['cli_anything.daily'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-daily=cli_anything.daily:cli']},
)
