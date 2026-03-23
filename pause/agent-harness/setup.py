from setuptools import setup
setup(
    name='cli-anything-pause',
    version='1.0.0',
    packages=['cli_anything.pause'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pause=cli_anything.pause:cli']},
)
