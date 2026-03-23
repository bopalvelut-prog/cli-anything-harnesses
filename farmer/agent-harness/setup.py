from setuptools import setup
setup(
    name='cli-anything-farmer',
    version='1.0.0',
    packages=['cli_anything.farmer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-farmer=cli_anything.farmer:cli']},
)
