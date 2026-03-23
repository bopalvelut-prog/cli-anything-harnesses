from setuptools import setup
setup(
    name='cli-anything-croc',
    version='1.0.0',
    packages=['cli_anything.croc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-croc=cli_anything.croc:cli']},
)
