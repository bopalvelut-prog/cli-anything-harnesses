from setuptools import setup
setup(
    name='cli-anything-outer',
    version='1.0.0',
    packages=['cli_anything.outer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outer=cli_anything.outer:cli']},
)
