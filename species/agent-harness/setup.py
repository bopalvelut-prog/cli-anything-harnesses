from setuptools import setup
setup(
    name='cli-anything-species',
    version='1.0.0',
    packages=['cli_anything.species'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-species=cli_anything.species:cli']},
)
