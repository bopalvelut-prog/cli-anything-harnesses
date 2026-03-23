from setuptools import setup
setup(
    name='cli-anything-rogue',
    version='1.0.0',
    packages=['cli_anything.rogue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rogue=cli_anything.rogue:cli']},
)
