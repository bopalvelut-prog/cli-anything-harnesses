from setuptools import setup
setup(
    name='cli-anything-adaptive',
    version='1.0.0',
    packages=['cli_anything.adaptive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adaptive=cli_anything.adaptive:cli']},
)
