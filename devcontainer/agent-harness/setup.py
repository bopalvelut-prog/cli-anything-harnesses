from setuptools import setup
setup(
    name='cli-anything-devcontainer',
    version='1.0.0',
    packages=['cli_anything.devcontainer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devcontainer=cli_anything.devcontainer:cli']},
)
