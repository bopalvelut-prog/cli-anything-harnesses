from setuptools import setup
setup(
    name='cli-anything-night',
    version='1.0.0',
    packages=['cli_anything.night'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-night=cli_anything.night:cli']},
)
