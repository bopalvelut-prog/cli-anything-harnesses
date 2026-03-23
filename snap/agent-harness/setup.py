from setuptools import setup
setup(
    name='cli-anything-snap',
    version='1.0.0',
    packages=['cli_anything.snap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snap=cli_anything.snap:cli']},
)
