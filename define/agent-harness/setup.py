from setuptools import setup
setup(
    name='cli-anything-define',
    version='1.0.0',
    packages=['cli_anything.define'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-define=cli_anything.define:cli']},
)
