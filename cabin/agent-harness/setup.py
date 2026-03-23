from setuptools import setup
setup(
    name='cli-anything-cabin',
    version='1.0.0',
    packages=['cli_anything.cabin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cabin=cli_anything.cabin:cli']},
)
