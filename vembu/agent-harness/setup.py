from setuptools import setup
setup(
    name='cli-anything-vembu',
    version='1.0.0',
    packages=['cli_anything.vembu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vembu=cli_anything.vembu:cli']},
)
