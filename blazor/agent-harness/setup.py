from setuptools import setup
setup(
    name='cli-anything-blazor',
    version='1.0.0',
    packages=['cli_anything.blazor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blazor=cli_anything.blazor:cli']},
)
