from setuptools import setup
setup(
    name='cli-anything-probe',
    version='1.0.0',
    packages=['cli_anything.probe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-probe=cli_anything.probe:cli']},
)
