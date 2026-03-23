from setuptools import setup
setup(
    name='cli-anything-bay',
    version='1.0.0',
    packages=['cli_anything.bay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bay=cli_anything.bay:cli']},
)
