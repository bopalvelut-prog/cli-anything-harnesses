from setuptools import setup
setup(
    name='cli-anything-possible',
    version='1.0.0',
    packages=['cli_anything.possible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-possible=cli_anything.possible:cli']},
)
