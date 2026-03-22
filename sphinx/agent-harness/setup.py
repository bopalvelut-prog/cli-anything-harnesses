from setuptools import setup
setup(
    name='cli-anything-sphinx',
    version='1.0.0',
    packages=['cli_anything.sphinx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sphinx=cli_anything.sphinx:cli']},
)
