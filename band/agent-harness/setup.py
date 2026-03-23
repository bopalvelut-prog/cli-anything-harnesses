from setuptools import setup
setup(
    name='cli-anything-band',
    version='1.0.0',
    packages=['cli_anything.band'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-band=cli_anything.band:cli']},
)
