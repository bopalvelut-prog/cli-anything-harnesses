from setuptools import setup
setup(
    name='cli-anything-bound',
    version='1.0.0',
    packages=['cli_anything.bound'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bound=cli_anything.bound:cli']},
)
