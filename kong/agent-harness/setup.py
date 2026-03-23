from setuptools import setup
setup(
    name='cli-anything-kong',
    version='1.0.0',
    packages=['cli_anything.kong'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kong=cli_anything.kong:cli']},
)
