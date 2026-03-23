from setuptools import setup
setup(
    name='cli-anything-timescale',
    version='1.0.0',
    packages=['cli_anything.timescale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timescale=cli_anything.timescale:cli']},
)
