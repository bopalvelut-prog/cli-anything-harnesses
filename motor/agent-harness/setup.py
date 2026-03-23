from setuptools import setup
setup(
    name='cli-anything-motor',
    version='1.0.0',
    packages=['cli_anything.motor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-motor=cli_anything.motor:cli']},
)
