from setuptools import setup
setup(
    name='cli-anything-astral',
    version='1.0.0',
    packages=['cli_anything.astral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-astral=cli_anything.astral:cli']},
)
