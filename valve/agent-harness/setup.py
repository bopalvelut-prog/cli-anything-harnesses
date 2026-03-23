from setuptools import setup
setup(
    name='cli-anything-valve',
    version='1.0.0',
    packages=['cli_anything.valve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-valve=cli_anything.valve:cli']},
)
