from setuptools import setup
setup(
    name='cli-anything-passion',
    version='1.0.0',
    packages=['cli_anything.passion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-passion=cli_anything.passion:cli']},
)
