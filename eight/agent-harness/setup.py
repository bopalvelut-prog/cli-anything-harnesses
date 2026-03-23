from setuptools import setup
setup(
    name='cli-anything-eight',
    version='1.0.0',
    packages=['cli_anything.eight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eight=cli_anything.eight:cli']},
)
