from setuptools import setup
setup(
    name='cli-anything-simulation',
    version='1.0.0',
    packages=['cli_anything.simulation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-simulation=cli_anything.simulation:cli']},
)
