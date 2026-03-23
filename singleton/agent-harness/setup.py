from setuptools import setup
setup(
    name='cli-anything-singleton',
    version='1.0.0',
    packages=['cli_anything.singleton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-singleton=cli_anything.singleton:cli']},
)
