from setuptools import setup
setup(
    name='cli-anything-google_maps',
    version='1.0.0',
    packages=['cli_anything.google_maps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_maps=cli_anything.google_maps:cli']},
)
