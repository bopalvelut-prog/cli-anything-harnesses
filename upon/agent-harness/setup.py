from setuptools import setup
setup(
    name='cli-anything-upon',
    version='1.0.0',
    packages=['cli_anything.upon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-upon=cli_anything.upon:cli']},
)
