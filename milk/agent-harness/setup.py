from setuptools import setup
setup(
    name='cli-anything-milk',
    version='1.0.0',
    packages=['cli_anything.milk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-milk=cli_anything.milk:cli']},
)
