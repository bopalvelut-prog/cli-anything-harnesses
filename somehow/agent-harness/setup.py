from setuptools import setup
setup(
    name='cli-anything-somehow',
    version='1.0.0',
    packages=['cli_anything.somehow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-somehow=cli_anything.somehow:cli']},
)
