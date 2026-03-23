from setuptools import setup
setup(
    name='cli-anything-settlement',
    version='1.0.0',
    packages=['cli_anything.settlement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-settlement=cli_anything.settlement:cli']},
)
