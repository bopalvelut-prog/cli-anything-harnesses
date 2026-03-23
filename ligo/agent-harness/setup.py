from setuptools import setup
setup(
    name='cli-anything-ligo',
    version='1.0.0',
    packages=['cli_anything.ligo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ligo=cli_anything.ligo:cli']},
)
