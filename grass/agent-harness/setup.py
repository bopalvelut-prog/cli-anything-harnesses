from setuptools import setup
setup(
    name='cli-anything-grass',
    version='1.0.0',
    packages=['cli_anything.grass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grass=cli_anything.grass:cli']},
)
