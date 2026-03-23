from setuptools import setup
setup(
    name='cli-anything-fight',
    version='1.0.0',
    packages=['cli_anything.fight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fight=cli_anything.fight:cli']},
)
