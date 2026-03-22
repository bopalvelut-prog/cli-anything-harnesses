from setuptools import setup
setup(
    name='cli-anything-matrix',
    version='1.0.0',
    packages=['cli_anything.matrix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-matrix=cli_anything.matrix:cli']},
)
