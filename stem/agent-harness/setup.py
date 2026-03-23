from setuptools import setup
setup(
    name='cli-anything-stem',
    version='1.0.0',
    packages=['cli_anything.stem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stem=cli_anything.stem:cli']},
)
