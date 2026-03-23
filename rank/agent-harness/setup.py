from setuptools import setup
setup(
    name='cli-anything-rank',
    version='1.0.0',
    packages=['cli_anything.rank'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rank=cli_anything.rank:cli']},
)
