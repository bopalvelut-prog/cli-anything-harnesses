from setuptools import setup
setup(
    name='cli-anything-compare',
    version='1.0.0',
    packages=['cli_anything.compare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-compare=cli_anything.compare:cli']},
)
