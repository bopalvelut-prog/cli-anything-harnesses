from setuptools import setup
setup(
    name='cli-anything-map',
    version='1.0.0',
    packages=['cli_anything.map'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-map=cli_anything.map:cli']},
)
