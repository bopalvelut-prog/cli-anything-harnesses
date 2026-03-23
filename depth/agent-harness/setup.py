from setuptools import setup
setup(
    name='cli-anything-depth',
    version='1.0.0',
    packages=['cli_anything.depth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-depth=cli_anything.depth:cli']},
)
