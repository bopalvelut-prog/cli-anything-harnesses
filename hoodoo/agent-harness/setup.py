from setuptools import setup
setup(
    name='cli-anything-hoodoo',
    version='1.0.0',
    packages=['cli_anything.hoodoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hoodoo=cli_anything.hoodoo:cli']},
)
