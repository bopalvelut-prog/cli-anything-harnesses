from setuptools import setup
setup(
    name='cli-anything-cloth',
    version='1.0.0',
    packages=['cli_anything.cloth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloth=cli_anything.cloth:cli']},
)
