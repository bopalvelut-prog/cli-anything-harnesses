from setuptools import setup
setup(
    name='cli-anything-stare',
    version='1.0.0',
    packages=['cli_anything.stare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stare=cli_anything.stare:cli']},
)
