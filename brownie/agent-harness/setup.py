from setuptools import setup
setup(
    name='cli-anything-brownie',
    version='1.0.0',
    packages=['cli_anything.brownie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brownie=cli_anything.brownie:cli']},
)
