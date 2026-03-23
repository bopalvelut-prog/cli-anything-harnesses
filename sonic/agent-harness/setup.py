from setuptools import setup
setup(
    name='cli-anything-sonic',
    version='1.0.0',
    packages=['cli_anything.sonic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonic=cli_anything.sonic:cli']},
)
