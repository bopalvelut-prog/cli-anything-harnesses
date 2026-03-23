from setuptools import setup
setup(
    name='cli-anything-round',
    version='1.0.0',
    packages=['cli_anything.round'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-round=cli_anything.round:cli']},
)
