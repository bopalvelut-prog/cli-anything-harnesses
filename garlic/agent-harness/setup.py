from setuptools import setup
setup(
    name='cli-anything-garlic',
    version='1.0.0',
    packages=['cli_anything.garlic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-garlic=cli_anything.garlic:cli']},
)
