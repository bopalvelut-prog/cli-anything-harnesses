from setuptools import setup
setup(
    name='cli-anything-thing',
    version='1.0.0',
    packages=['cli_anything.thing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thing=cli_anything.thing:cli']},
)
