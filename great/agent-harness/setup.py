from setuptools import setup
setup(
    name='cli-anything-great',
    version='1.0.0',
    packages=['cli_anything.great'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-great=cli_anything.great:cli']},
)
