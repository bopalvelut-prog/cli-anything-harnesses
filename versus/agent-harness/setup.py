from setuptools import setup
setup(
    name='cli-anything-versus',
    version='1.0.0',
    packages=['cli_anything.versus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-versus=cli_anything.versus:cli']},
)
