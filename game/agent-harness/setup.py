from setuptools import setup
setup(
    name='cli-anything-game',
    version='1.0.0',
    packages=['cli_anything.game'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-game=cli_anything.game:cli']},
)
