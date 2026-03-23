from setuptools import setup
setup(
    name='cli-anything-vehicle',
    version='1.0.0',
    packages=['cli_anything.vehicle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vehicle=cli_anything.vehicle:cli']},
)
