from setuptools import setup
setup(
    name='cli-anything-elevate',
    version='1.0.0',
    packages=['cli_anything.elevate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elevate=cli_anything.elevate:cli']},
)
