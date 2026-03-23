from setuptools import setup
setup(
    name='cli-anything-extract',
    version='1.0.0',
    packages=['cli_anything.extract'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-extract=cli_anything.extract:cli']},
)
