from setuptools import setup
setup(
    name='cli-anything-roll',
    version='1.0.0',
    packages=['cli_anything.roll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roll=cli_anything.roll:cli']},
)
