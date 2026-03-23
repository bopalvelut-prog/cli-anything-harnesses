from setuptools import setup
setup(
    name='cli-anything-atari',
    version='1.0.0',
    packages=['cli_anything.atari'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atari=cli_anything.atari:cli']},
)
