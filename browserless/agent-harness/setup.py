from setuptools import setup
setup(
    name='cli-anything-browserless',
    version='1.0.0',
    packages=['cli_anything.browserless'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-browserless=cli_anything.browserless:cli']},
)
