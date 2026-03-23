from setuptools import setup
setup(
    name='cli-anything-wizard',
    version='1.0.0',
    packages=['cli_anything.wizard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wizard=cli_anything.wizard:cli']},
)
