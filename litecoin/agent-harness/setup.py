from setuptools import setup
setup(
    name='cli-anything-litecoin',
    version='1.0.0',
    packages=['cli_anything.litecoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-litecoin=cli_anything.litecoin:cli']},
)
