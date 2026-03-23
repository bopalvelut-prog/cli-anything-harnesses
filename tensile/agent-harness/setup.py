from setuptools import setup
setup(
    name='cli-anything-tensile',
    version='1.0.0',
    packages=['cli_anything.tensile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tensile=cli_anything.tensile:cli']},
)
