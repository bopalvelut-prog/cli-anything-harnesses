from setuptools import setup
setup(
    name='cli-anything-lost',
    version='1.0.0',
    packages=['cli_anything.lost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lost=cli_anything.lost:cli']},
)
