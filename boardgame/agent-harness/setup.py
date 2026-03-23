from setuptools import setup
setup(
    name='cli-anything-boardgame',
    version='1.0.0',
    packages=['cli_anything.boardgame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boardgame=cli_anything.boardgame:cli']},
)
