from setuptools import setup
setup(
    name='cli-anything-npm',
    version='1.0.0',
    packages=['cli_anything.npm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-npm=cli_anything.npm:cli']},
)
