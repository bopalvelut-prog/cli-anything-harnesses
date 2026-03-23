from setuptools import setup
setup(
    name='cli-anything-genius',
    version='1.0.0',
    packages=['cli_anything.genius'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-genius=cli_anything.genius:cli']},
)
