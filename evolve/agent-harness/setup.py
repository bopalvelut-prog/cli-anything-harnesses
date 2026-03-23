from setuptools import setup
setup(
    name='cli-anything-evolve',
    version='1.0.0',
    packages=['cli_anything.evolve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-evolve=cli_anything.evolve:cli']},
)
