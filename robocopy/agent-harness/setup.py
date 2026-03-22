from setuptools import setup
setup(
    name='cli-anything-robocopy',
    version='1.0.0',
    packages=['cli_anything.robocopy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-robocopy=cli_anything.robocopy:cli']},
)
