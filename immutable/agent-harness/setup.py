from setuptools import setup
setup(
    name='cli-anything-immutable',
    version='1.0.0',
    packages=['cli_anything.immutable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-immutable=cli_anything.immutable:cli']},
)
