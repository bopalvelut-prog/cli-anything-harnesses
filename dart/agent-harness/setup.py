from setuptools import setup
setup(
    name='cli-anything-dart',
    version='1.0.0',
    packages=['cli_anything.dart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dart=cli_anything.dart:cli']},
)
