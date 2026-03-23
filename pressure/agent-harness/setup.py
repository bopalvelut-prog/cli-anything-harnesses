from setuptools import setup
setup(
    name='cli-anything-pressure',
    version='1.0.0',
    packages=['cli_anything.pressure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pressure=cli_anything.pressure:cli']},
)
