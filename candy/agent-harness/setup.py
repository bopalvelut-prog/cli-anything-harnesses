from setuptools import setup
setup(
    name='cli-anything-candy',
    version='1.0.0',
    packages=['cli_anything.candy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-candy=cli_anything.candy:cli']},
)
