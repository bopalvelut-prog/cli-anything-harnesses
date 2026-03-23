from setuptools import setup
setup(
    name='cli-anything-banana',
    version='1.0.0',
    packages=['cli_anything.banana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-banana=cli_anything.banana:cli']},
)
