from setuptools import setup
setup(
    name='cli-anything-tired',
    version='1.0.0',
    packages=['cli_anything.tired'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tired=cli_anything.tired:cli']},
)
