from setuptools import setup
setup(
    name='cli-anything-roller',
    version='1.0.0',
    packages=['cli_anything.roller'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roller=cli_anything.roller:cli']},
)
