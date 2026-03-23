from setuptools import setup
setup(
    name='cli-anything-hard',
    version='1.0.0',
    packages=['cli_anything.hard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hard=cli_anything.hard:cli']},
)
