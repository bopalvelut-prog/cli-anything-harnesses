from setuptools import setup
setup(
    name='cli-anything-agile',
    version='1.0.0',
    packages=['cli_anything.agile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agile=cli_anything.agile:cli']},
)
