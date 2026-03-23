from setuptools import setup
setup(
    name='cli-anything-divide',
    version='1.0.0',
    packages=['cli_anything.divide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-divide=cli_anything.divide:cli']},
)
