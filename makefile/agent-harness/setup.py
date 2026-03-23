from setuptools import setup
setup(
    name='cli-anything-makefile',
    version='1.0.0',
    packages=['cli_anything.makefile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-makefile=cli_anything.makefile:cli']},
)
