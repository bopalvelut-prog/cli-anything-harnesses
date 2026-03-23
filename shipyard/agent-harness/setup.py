from setuptools import setup
setup(
    name='cli-anything-shipyard',
    version='1.0.0',
    packages=['cli_anything.shipyard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shipyard=cli_anything.shipyard:cli']},
)
