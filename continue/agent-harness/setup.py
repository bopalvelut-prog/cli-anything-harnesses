from setuptools import setup
setup(
    name='cli-anything-continue',
    version='1.0.0',
    packages=['cli_anything.continue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-continue=cli_anything.continue:cli']},
)
