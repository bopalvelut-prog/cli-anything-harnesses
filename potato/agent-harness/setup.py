from setuptools import setup
setup(
    name='cli-anything-potato',
    version='1.0.0',
    packages=['cli_anything.potato'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-potato=cli_anything.potato:cli']},
)
