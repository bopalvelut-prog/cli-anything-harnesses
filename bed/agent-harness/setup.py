from setuptools import setup
setup(
    name='cli-anything-bed',
    version='1.0.0',
    packages=['cli_anything.bed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bed=cli_anything.bed:cli']},
)
