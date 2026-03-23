from setuptools import setup
setup(
    name='cli-anything-agones',
    version='1.0.0',
    packages=['cli_anything.agones'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agones=cli_anything.agones:cli']},
)
