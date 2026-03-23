from setuptools import setup
setup(
    name='cli-anything-tame',
    version='1.0.0',
    packages=['cli_anything.tame'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tame=cli_anything.tame:cli']},
)
