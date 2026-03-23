from setuptools import setup
setup(
    name='cli-anything-deck',
    version='1.0.0',
    packages=['cli_anything.deck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deck=cli_anything.deck:cli']},
)
