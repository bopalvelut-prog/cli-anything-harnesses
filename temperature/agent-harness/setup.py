from setuptools import setup
setup(
    name='cli-anything-temperature',
    version='1.0.0',
    packages=['cli_anything.temperature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-temperature=cli_anything.temperature:cli']},
)
