from setuptools import setup
setup(
    name='cli-anything-engage',
    version='1.0.0',
    packages=['cli_anything.engage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-engage=cli_anything.engage:cli']},
)
