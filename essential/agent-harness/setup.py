from setuptools import setup
setup(
    name='cli-anything-essential',
    version='1.0.0',
    packages=['cli_anything.essential'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-essential=cli_anything.essential:cli']},
)
