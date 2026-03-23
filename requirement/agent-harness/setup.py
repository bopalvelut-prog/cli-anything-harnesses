from setuptools import setup
setup(
    name='cli-anything-requirement',
    version='1.0.0',
    packages=['cli_anything.requirement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-requirement=cli_anything.requirement:cli']},
)
