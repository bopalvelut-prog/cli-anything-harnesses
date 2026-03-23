from setuptools import setup
setup(
    name='cli-anything-geoip',
    version='1.0.0',
    packages=['cli_anything.geoip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-geoip=cli_anything.geoip:cli']},
)
