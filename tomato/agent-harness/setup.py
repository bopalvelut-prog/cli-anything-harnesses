from setuptools import setup
setup(
    name='cli-anything-tomato',
    version='1.0.0',
    packages=['cli_anything.tomato'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tomato=cli_anything.tomato:cli']},
)
