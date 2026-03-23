from setuptools import setup
setup(
    name='cli-anything-deputy',
    version='1.0.0',
    packages=['cli_anything.deputy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deputy=cli_anything.deputy:cli']},
)
