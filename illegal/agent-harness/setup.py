from setuptools import setup
setup(
    name='cli-anything-illegal',
    version='1.0.0',
    packages=['cli_anything.illegal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-illegal=cli_anything.illegal:cli']},
)
