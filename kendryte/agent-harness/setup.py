from setuptools import setup
setup(
    name='cli-anything-kendryte',
    version='1.0.0',
    packages=['cli_anything.kendryte'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kendryte=cli_anything.kendryte:cli']},
)
