from setuptools import setup
setup(
    name='cli-anything-conduct',
    version='1.0.0',
    packages=['cli_anything.conduct'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conduct=cli_anything.conduct:cli']},
)
