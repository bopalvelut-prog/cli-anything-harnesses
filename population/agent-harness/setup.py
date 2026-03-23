from setuptools import setup
setup(
    name='cli-anything-population',
    version='1.0.0',
    packages=['cli_anything.population'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-population=cli_anything.population:cli']},
)
