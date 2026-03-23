from setuptools import setup
setup(
    name='cli-anything-best',
    version='1.0.0',
    packages=['cli_anything.best'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-best=cli_anything.best:cli']},
)
