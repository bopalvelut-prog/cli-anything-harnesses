from setuptools import setup
setup(
    name='cli-anything-remain',
    version='1.0.0',
    packages=['cli_anything.remain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remain=cli_anything.remain:cli']},
)
