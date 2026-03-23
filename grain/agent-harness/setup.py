from setuptools import setup
setup(
    name='cli-anything-grain',
    version='1.0.0',
    packages=['cli_anything.grain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grain=cli_anything.grain:cli']},
)
