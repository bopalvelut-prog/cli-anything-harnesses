from setuptools import setup
setup(
    name='cli-anything-orca',
    version='1.0.0',
    packages=['cli_anything.orca'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-orca=cli_anything.orca:cli']},
)
