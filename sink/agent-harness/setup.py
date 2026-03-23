from setuptools import setup
setup(
    name='cli-anything-sink',
    version='1.0.0',
    packages=['cli_anything.sink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sink=cli_anything.sink:cli']},
)
