from setuptools import setup
setup(
    name='cli-anything-narrative',
    version='1.0.0',
    packages=['cli_anything.narrative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-narrative=cli_anything.narrative:cli']},
)
