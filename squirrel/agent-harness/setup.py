from setuptools import setup
setup(
    name='cli-anything-squirrel',
    version='1.0.0',
    packages=['cli_anything.squirrel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-squirrel=cli_anything.squirrel:cli']},
)
