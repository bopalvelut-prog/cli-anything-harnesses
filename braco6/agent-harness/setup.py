from setuptools import setup
setup(
    name='cli-anything-braco6',
    version='1.0.0',
    packages=['cli_anything.braco6'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco6=cli_anything.braco6:cli']},
)
