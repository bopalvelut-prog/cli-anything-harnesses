from setuptools import setup
setup(
    name='cli-anything-coin',
    version='1.0.0',
    packages=['cli_anything.coin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coin=cli_anything.coin:cli']},
)
