from setuptools import setup
setup(
    name='cli-anything-astar',
    version='1.0.0',
    packages=['cli_anything.astar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-astar=cli_anything.astar:cli']},
)
