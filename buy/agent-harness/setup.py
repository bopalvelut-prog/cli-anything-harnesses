from setuptools import setup
setup(
    name='cli-anything-buy',
    version='1.0.0',
    packages=['cli_anything.buy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buy=cli_anything.buy:cli']},
)
