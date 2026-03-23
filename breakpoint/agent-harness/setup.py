from setuptools import setup
setup(
    name='cli-anything-breakpoint',
    version='1.0.0',
    packages=['cli_anything.breakpoint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-breakpoint=cli_anything.breakpoint:cli']},
)
