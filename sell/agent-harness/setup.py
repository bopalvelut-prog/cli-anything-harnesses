from setuptools import setup
setup(
    name='cli-anything-sell',
    version='1.0.0',
    packages=['cli_anything.sell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sell=cli_anything.sell:cli']},
)
