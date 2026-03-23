from setuptools import setup
setup(
    name='cli-anything-soup',
    version='1.0.0',
    packages=['cli_anything.soup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soup=cli_anything.soup:cli']},
)
