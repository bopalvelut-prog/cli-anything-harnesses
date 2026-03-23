from setuptools import setup
setup(
    name='cli-anything-osrm',
    version='1.0.0',
    packages=['cli_anything.osrm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-osrm=cli_anything.osrm:cli']},
)
