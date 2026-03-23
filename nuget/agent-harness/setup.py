from setuptools import setup
setup(
    name='cli-anything-nuget',
    version='1.0.0',
    packages=['cli_anything.nuget'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nuget=cli_anything.nuget:cli']},
)
