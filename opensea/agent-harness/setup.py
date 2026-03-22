from setuptools import setup
setup(
    name='cli-anything-opensea',
    version='1.0.0',
    packages=['cli_anything.opensea'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opensea=cli_anything.opensea:cli']},
)
