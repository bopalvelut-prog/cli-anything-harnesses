from setuptools import setup
setup(
    name='cli-anything-realize',
    version='1.0.0',
    packages=['cli_anything.realize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-realize=cli_anything.realize:cli']},
)
