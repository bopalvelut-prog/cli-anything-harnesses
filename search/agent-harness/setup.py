from setuptools import setup
setup(
    name='cli-anything-search',
    version='1.0.0',
    packages=['cli_anything.search'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-search=cli_anything.search:cli']},
)
