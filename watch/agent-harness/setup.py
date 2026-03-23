from setuptools import setup
setup(
    name='cli-anything-watch',
    version='1.0.0',
    packages=['cli_anything.watch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-watch=cli_anything.watch:cli']},
)
