from setuptools import setup
setup(
    name='cli-anything-nem',
    version='1.0.0',
    packages=['cli_anything.nem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nem=cli_anything.nem:cli']},
)
