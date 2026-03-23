from setuptools import setup
setup(
    name='cli-anything-ng',
    version='1.0.0',
    packages=['cli_anything.ng'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ng=cli_anything.ng:cli']},
)
