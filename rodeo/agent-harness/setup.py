from setuptools import setup
setup(
    name='cli-anything-rodeo',
    version='1.0.0',
    packages=['cli_anything.rodeo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rodeo=cli_anything.rodeo:cli']},
)
