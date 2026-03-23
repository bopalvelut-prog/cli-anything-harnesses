from setuptools import setup
setup(
    name='cli-anything-algernon',
    version='1.0.0',
    packages=['cli_anything.algernon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-algernon=cli_anything.algernon:cli']},
)
