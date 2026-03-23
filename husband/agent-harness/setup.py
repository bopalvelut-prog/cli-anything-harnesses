from setuptools import setup
setup(
    name='cli-anything-husband',
    version='1.0.0',
    packages=['cli_anything.husband'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-husband=cli_anything.husband:cli']},
)
