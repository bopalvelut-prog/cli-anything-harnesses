from setuptools import setup
setup(
    name='cli-anything-amber',
    version='1.0.0',
    packages=['cli_anything.amber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amber=cli_anything.amber:cli']},
)
