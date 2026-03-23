from setuptools import setup
setup(
    name='cli-anything-ugly',
    version='1.0.0',
    packages=['cli_anything.ugly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ugly=cli_anything.ugly:cli']},
)
