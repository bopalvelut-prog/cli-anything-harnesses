from setuptools import setup
setup(
    name='cli-anything-pipe',
    version='1.0.0',
    packages=['cli_anything.pipe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pipe=cli_anything.pipe:cli']},
)
