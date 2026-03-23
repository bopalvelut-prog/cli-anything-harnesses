from setuptools import setup
setup(
    name='cli-anything-biome',
    version='1.0.0',
    packages=['cli_anything.biome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-biome=cli_anything.biome:cli']},
)
