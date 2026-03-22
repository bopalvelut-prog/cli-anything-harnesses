from setuptools import setup
setup(
    name='cli-anything-mediawiki',
    version='1.0.0',
    packages=['cli_anything.mediawiki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mediawiki=cli_anything.mediawiki:cli']},
)
