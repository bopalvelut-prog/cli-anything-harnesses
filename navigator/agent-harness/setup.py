from setuptools import setup
setup(
    name='cli-anything-navigator',
    version='1.0.0',
    packages=['cli_anything.navigator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-navigator=cli_anything.navigator:cli']},
)
