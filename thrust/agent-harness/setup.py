from setuptools import setup
setup(
    name='cli-anything-thrust',
    version='1.0.0',
    packages=['cli_anything.thrust'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thrust=cli_anything.thrust:cli']},
)
