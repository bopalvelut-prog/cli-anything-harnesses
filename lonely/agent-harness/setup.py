from setuptools import setup
setup(
    name='cli-anything-lonely',
    version='1.0.0',
    packages=['cli_anything.lonely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lonely=cli_anything.lonely:cli']},
)
