from setuptools import setup
setup(
    name='cli-anything-now',
    version='1.0.0',
    packages=['cli_anything.now'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-now=cli_anything.now:cli']},
)
