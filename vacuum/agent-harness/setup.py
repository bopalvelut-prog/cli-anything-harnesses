from setuptools import setup
setup(
    name='cli-anything-vacuum',
    version='1.0.0',
    packages=['cli_anything.vacuum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vacuum=cli_anything.vacuum:cli']},
)
