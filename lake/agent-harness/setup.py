from setuptools import setup
setup(
    name='cli-anything-lake',
    version='1.0.0',
    packages=['cli_anything.lake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lake=cli_anything.lake:cli']},
)
