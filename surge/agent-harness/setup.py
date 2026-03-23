from setuptools import setup
setup(
    name='cli-anything-surge',
    version='1.0.0',
    packages=['cli_anything.surge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surge=cli_anything.surge:cli']},
)
