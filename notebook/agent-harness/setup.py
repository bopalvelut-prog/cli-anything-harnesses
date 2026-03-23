from setuptools import setup
setup(
    name='cli-anything-notebook',
    version='1.0.0',
    packages=['cli_anything.notebook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-notebook=cli_anything.notebook:cli']},
)
