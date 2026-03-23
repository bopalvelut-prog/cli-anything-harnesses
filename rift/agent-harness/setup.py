from setuptools import setup
setup(
    name='cli-anything-rift',
    version='1.0.0',
    packages=['cli_anything.rift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rift=cli_anything.rift:cli']},
)
