from setuptools import setup
setup(
    name='cli-anything-selection',
    version='1.0.0',
    packages=['cli_anything.selection'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-selection=cli_anything.selection:cli']},
)
