from setuptools import setup
setup(
    name='cli-anything-physical',
    version='1.0.0',
    packages=['cli_anything.physical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-physical=cli_anything.physical:cli']},
)
