from setuptools import setup
setup(
    name='cli-anything-league',
    version='1.0.0',
    packages=['cli_anything.league'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-league=cli_anything.league:cli']},
)
