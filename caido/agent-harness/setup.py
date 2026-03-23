from setuptools import setup
setup(
    name='cli-anything-caido',
    version='1.0.0',
    packages=['cli_anything.caido'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-caido=cli_anything.caido:cli']},
)
