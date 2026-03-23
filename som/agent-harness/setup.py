from setuptools import setup
setup(
    name='cli-anything-som',
    version='1.0.0',
    packages=['cli_anything.som'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-som=cli_anything.som:cli']},
)
