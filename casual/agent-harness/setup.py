from setuptools import setup
setup(
    name='cli-anything-casual',
    version='1.0.0',
    packages=['cli_anything.casual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-casual=cli_anything.casual:cli']},
)
