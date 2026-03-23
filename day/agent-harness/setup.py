from setuptools import setup
setup(
    name='cli-anything-day',
    version='1.0.0',
    packages=['cli_anything.day'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-day=cli_anything.day:cli']},
)
