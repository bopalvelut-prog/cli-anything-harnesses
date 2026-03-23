from setuptools import setup
setup(
    name='cli-anything-exercise',
    version='1.0.0',
    packages=['cli_anything.exercise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exercise=cli_anything.exercise:cli']},
)
