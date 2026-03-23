from setuptools import setup
setup(
    name='cli-anything-builder',
    version='1.0.0',
    packages=['cli_anything.builder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-builder=cli_anything.builder:cli']},
)
