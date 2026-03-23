from setuptools import setup
setup(
    name='cli-anything-quiet',
    version='1.0.0',
    packages=['cli_anything.quiet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quiet=cli_anything.quiet:cli']},
)
