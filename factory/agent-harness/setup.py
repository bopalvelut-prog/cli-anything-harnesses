from setuptools import setup
setup(
    name='cli-anything-factory',
    version='1.0.0',
    packages=['cli_anything.factory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-factory=cli_anything.factory:cli']},
)
