from setuptools import setup
setup(
    name='cli-anything-princess',
    version='1.0.0',
    packages=['cli_anything.princess'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-princess=cli_anything.princess:cli']},
)
