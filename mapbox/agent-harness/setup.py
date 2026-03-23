from setuptools import setup
setup(
    name='cli-anything-mapbox',
    version='1.0.0',
    packages=['cli_anything.mapbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mapbox=cli_anything.mapbox:cli']},
)
