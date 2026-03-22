from setuptools import setup
setup(
    name='cli-anything-compound',
    version='1.0.0',
    packages=['cli_anything.compound'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-compound=cli_anything.compound:cli']},
)
