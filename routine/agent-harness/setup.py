from setuptools import setup
setup(
    name='cli-anything-routine',
    version='1.0.0',
    packages=['cli_anything.routine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-routine=cli_anything.routine:cli']},
)
