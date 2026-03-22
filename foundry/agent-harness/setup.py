from setuptools import setup
setup(
    name='cli-anything-foundry',
    version='1.0.0',
    packages=['cli_anything.foundry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-foundry=cli_anything.foundry:cli']},
)
