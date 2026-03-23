from setuptools import setup
setup(
    name='cli-anything-board',
    version='1.0.0',
    packages=['cli_anything.board'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-board=cli_anything.board:cli']},
)
