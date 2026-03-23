from setuptools import setup
setup(
    name='cli-anything-final',
    version='1.0.0',
    packages=['cli_anything.final'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-final=cli_anything.final:cli']},
)
