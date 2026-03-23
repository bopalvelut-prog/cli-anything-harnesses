from setuptools import setup
setup(
    name='cli-anything-artifact',
    version='1.0.0',
    packages=['cli_anything.artifact'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-artifact=cli_anything.artifact:cli']},
)
