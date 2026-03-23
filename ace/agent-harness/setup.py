from setuptools import setup
setup(
    name='cli-anything-ace',
    version='1.0.0',
    packages=['cli_anything.ace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ace=cli_anything.ace:cli']},
)
