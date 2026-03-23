from setuptools import setup
setup(
    name='cli-anything-sourcemap',
    version='1.0.0',
    packages=['cli_anything.sourcemap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sourcemap=cli_anything.sourcemap:cli']},
)
