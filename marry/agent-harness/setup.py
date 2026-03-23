from setuptools import setup
setup(
    name='cli-anything-marry',
    version='1.0.0',
    packages=['cli_anything.marry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marry=cli_anything.marry:cli']},
)
