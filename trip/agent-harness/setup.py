from setuptools import setup
setup(
    name='cli-anything-trip',
    version='1.0.0',
    packages=['cli_anything.trip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trip=cli_anything.trip:cli']},
)
