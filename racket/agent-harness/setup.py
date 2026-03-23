from setuptools import setup
setup(
    name='cli-anything-racket',
    version='1.0.0',
    packages=['cli_anything.racket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-racket=cli_anything.racket:cli']},
)
