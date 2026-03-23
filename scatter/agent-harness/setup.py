from setuptools import setup
setup(
    name='cli-anything-scatter',
    version='1.0.0',
    packages=['cli_anything.scatter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scatter=cli_anything.scatter:cli']},
)
