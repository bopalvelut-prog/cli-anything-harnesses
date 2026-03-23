from setuptools import setup
setup(
    name='cli-anything-jetbrains',
    version='1.0.0',
    packages=['cli_anything.jetbrains'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jetbrains=cli_anything.jetbrains:cli']},
)
