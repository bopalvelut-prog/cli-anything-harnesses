from setuptools import setup
setup(
    name='cli-anything-money',
    version='1.0.0',
    packages=['cli_anything.money'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-money=cli_anything.money:cli']},
)
