from setuptools import setup
setup(
    name='cli-anything-roslyn',
    version='1.0.0',
    packages=['cli_anything.roslyn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roslyn=cli_anything.roslyn:cli']},
)
