from setuptools import setup
setup(
    name='cli-anything-childhood',
    version='1.0.0',
    packages=['cli_anything.childhood'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-childhood=cli_anything.childhood:cli']},
)
