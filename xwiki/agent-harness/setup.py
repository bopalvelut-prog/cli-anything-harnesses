from setuptools import setup
setup(
    name='cli-anything-xwiki',
    version='1.0.0',
    packages=['cli_anything.xwiki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xwiki=cli_anything.xwiki:cli']},
)
