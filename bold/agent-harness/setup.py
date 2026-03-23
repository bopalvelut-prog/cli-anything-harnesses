from setuptools import setup
setup(
    name='cli-anything-bold',
    version='1.0.0',
    packages=['cli_anything.bold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bold=cli_anything.bold:cli']},
)
