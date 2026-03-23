from setuptools import setup
setup(
    name='cli-anything-bomb',
    version='1.0.0',
    packages=['cli_anything.bomb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bomb=cli_anything.bomb:cli']},
)
