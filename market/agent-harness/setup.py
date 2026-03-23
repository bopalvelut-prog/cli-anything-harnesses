from setuptools import setup
setup(
    name='cli-anything-market',
    version='1.0.0',
    packages=['cli_anything.market'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-market=cli_anything.market:cli']},
)
