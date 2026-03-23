from setuptools import setup
setup(
    name='cli-anything-aom',
    version='1.0.0',
    packages=['cli_anything.aom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aom=cli_anything.aom:cli']},
)
