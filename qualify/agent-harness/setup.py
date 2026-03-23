from setuptools import setup
setup(
    name='cli-anything-qualify',
    version='1.0.0',
    packages=['cli_anything.qualify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qualify=cli_anything.qualify:cli']},
)
