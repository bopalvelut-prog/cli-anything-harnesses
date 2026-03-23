from setuptools import setup
setup(
    name='cli-anything-stuff',
    version='1.0.0',
    packages=['cli_anything.stuff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stuff=cli_anything.stuff:cli']},
)
