from setuptools import setup
setup(
    name='cli-anything-patrol',
    version='1.0.0',
    packages=['cli_anything.patrol'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-patrol=cli_anything.patrol:cli']},
)
