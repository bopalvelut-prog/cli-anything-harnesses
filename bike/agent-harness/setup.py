from setuptools import setup
setup(
    name='cli-anything-bike',
    version='1.0.0',
    packages=['cli_anything.bike'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bike=cli_anything.bike:cli']},
)
