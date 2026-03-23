from setuptools import setup
setup(
    name='cli-anything-wealth',
    version='1.0.0',
    packages=['cli_anything.wealth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wealth=cli_anything.wealth:cli']},
)
