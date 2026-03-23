from setuptools import setup
setup(
    name='cli-anything-house',
    version='1.0.0',
    packages=['cli_anything.house'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-house=cli_anything.house:cli']},
)
