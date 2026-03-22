from setuptools import setup
setup(
    name='cli-anything-lido',
    version='1.0.0',
    packages=['cli_anything.lido'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lido=cli_anything.lido:cli']},
)
