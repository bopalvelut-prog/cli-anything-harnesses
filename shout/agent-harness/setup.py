from setuptools import setup
setup(
    name='cli-anything-shout',
    version='1.0.0',
    packages=['cli_anything.shout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shout=cli_anything.shout:cli']},
)
