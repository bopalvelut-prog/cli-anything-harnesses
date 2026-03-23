from setuptools import setup
setup(
    name='cli-anything-simply',
    version='1.0.0',
    packages=['cli_anything.simply'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-simply=cli_anything.simply:cli']},
)
