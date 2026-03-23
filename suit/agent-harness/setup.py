from setuptools import setup
setup(
    name='cli-anything-suit',
    version='1.0.0',
    packages=['cli_anything.suit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suit=cli_anything.suit:cli']},
)
