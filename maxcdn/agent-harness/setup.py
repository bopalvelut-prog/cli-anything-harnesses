from setuptools import setup
setup(
    name='cli-anything-maxcdn',
    version='1.0.0',
    packages=['cli_anything.maxcdn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maxcdn=cli_anything.maxcdn:cli']},
)
