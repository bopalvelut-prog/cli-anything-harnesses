from setuptools import setup
setup(
    name='cli-anything-linux',
    version='1.0.0',
    packages=['cli_anything.linux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linux=cli_anything.linux:cli']},
)
