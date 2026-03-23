from setuptools import setup
setup(
    name='cli-anything-winter',
    version='1.0.0',
    packages=['cli_anything.winter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-winter=cli_anything.winter:cli']},
)
