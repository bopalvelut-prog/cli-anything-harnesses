from setuptools import setup
setup(
    name='cli-anything-typeorm',
    version='1.0.0',
    packages=['cli_anything.typeorm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typeorm=cli_anything.typeorm:cli']},
)
