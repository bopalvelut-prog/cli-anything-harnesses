from setuptools import setup
setup(
    name='cli-anything-ranch',
    version='1.0.0',
    packages=['cli_anything.ranch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ranch=cli_anything.ranch:cli']},
)
