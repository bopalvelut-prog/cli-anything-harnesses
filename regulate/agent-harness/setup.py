from setuptools import setup
setup(
    name='cli-anything-regulate',
    version='1.0.0',
    packages=['cli_anything.regulate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regulate=cli_anything.regulate:cli']},
)
