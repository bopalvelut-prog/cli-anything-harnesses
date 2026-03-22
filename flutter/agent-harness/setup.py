from setuptools import setup
setup(
    name='cli-anything-flutter',
    version='1.0.0',
    packages=['cli_anything.flutter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flutter=cli_anything.flutter:cli']},
)
