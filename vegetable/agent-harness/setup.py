from setuptools import setup
setup(
    name='cli-anything-vegetable',
    version='1.0.0',
    packages=['cli_anything.vegetable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vegetable=cli_anything.vegetable:cli']},
)
