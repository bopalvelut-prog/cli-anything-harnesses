from setuptools import setup
setup(
    name='cli-anything-turn',
    version='1.0.0',
    packages=['cli_anything.turn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turn=cli_anything.turn:cli']},
)
