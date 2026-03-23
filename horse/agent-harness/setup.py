from setuptools import setup
setup(
    name='cli-anything-horse',
    version='1.0.0',
    packages=['cli_anything.horse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-horse=cli_anything.horse:cli']},
)
