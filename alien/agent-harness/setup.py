from setuptools import setup
setup(
    name='cli-anything-alien',
    version='1.0.0',
    packages=['cli_anything.alien'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alien=cli_anything.alien:cli']},
)
