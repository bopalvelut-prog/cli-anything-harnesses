from setuptools import setup
setup(
    name='cli-anything-player',
    version='1.0.0',
    packages=['cli_anything.player'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-player=cli_anything.player:cli']},
)
