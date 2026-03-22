from setuptools import setup
setup(
    name='cli-anything-transmission',
    version='1.0.0',
    packages=['cli_anything.transmission'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transmission=cli_anything.transmission:cli']},
)
