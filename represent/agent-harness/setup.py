from setuptools import setup
setup(
    name='cli-anything-represent',
    version='1.0.0',
    packages=['cli_anything.represent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-represent=cli_anything.represent:cli']},
)
