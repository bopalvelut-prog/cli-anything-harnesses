from setuptools import setup
setup(
    name='cli-anything-piece',
    version='1.0.0',
    packages=['cli_anything.piece'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-piece=cli_anything.piece:cli']},
)
