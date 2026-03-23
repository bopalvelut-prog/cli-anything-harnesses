from setuptools import setup
setup(
    name='cli-anything-gelf',
    version='1.0.0',
    packages=['cli_anything.gelf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gelf=cli_anything.gelf:cli']},
)
