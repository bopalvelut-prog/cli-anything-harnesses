from setuptools import setup
setup(
    name='cli-anything-station',
    version='1.0.0',
    packages=['cli_anything.station'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-station=cli_anything.station:cli']},
)
