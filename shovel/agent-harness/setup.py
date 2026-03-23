from setuptools import setup
setup(
    name='cli-anything-shovel',
    version='1.0.0',
    packages=['cli_anything.shovel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shovel=cli_anything.shovel:cli']},
)
