from setuptools import setup
setup(
    name='cli-anything-pelias',
    version='1.0.0',
    packages=['cli_anything.pelias'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pelias=cli_anything.pelias:cli']},
)
