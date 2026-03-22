from setuptools import setup
setup(
    name='cli-anything-typeorm2',
    version='1.0.0',
    packages=['cli_anything.typeorm2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typeorm2=cli_anything.typeorm2:cli']},
)
