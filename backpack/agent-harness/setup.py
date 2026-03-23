from setuptools import setup
setup(
    name='cli-anything-backpack',
    version='1.0.0',
    packages=['cli_anything.backpack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-backpack=cli_anything.backpack:cli']},
)
