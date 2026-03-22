from setuptools import setup
setup(
    name='cli-anything-dokuwiki',
    version='1.0.0',
    packages=['cli_anything.dokuwiki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dokuwiki=cli_anything.dokuwiki:cli']},
)
