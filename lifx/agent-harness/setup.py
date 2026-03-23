from setuptools import setup
setup(
    name='cli-anything-lifx',
    version='1.0.0',
    packages=['cli_anything.lifx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lifx=cli_anything.lifx:cli']},
)
