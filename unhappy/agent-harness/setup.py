from setuptools import setup
setup(
    name='cli-anything-unhappy',
    version='1.0.0',
    packages=['cli_anything.unhappy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unhappy=cli_anything.unhappy:cli']},
)
