from setuptools import setup
setup(
    name='cli-anything-nomad',
    version='1.0.0',
    packages=['cli_anything.nomad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nomad=cli_anything.nomad:cli']},
)
