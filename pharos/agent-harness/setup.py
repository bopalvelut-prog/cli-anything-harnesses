from setuptools import setup
setup(
    name='cli-anything-pharos',
    version='1.0.0',
    packages=['cli_anything.pharos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pharos=cli_anything.pharos:cli']},
)
