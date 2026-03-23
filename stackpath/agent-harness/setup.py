from setuptools import setup
setup(
    name='cli-anything-stackpath',
    version='1.0.0',
    packages=['cli_anything.stackpath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stackpath=cli_anything.stackpath:cli']},
)
