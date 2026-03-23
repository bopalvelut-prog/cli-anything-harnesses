from setuptools import setup
setup(
    name='cli-anything-extreme',
    version='1.0.0',
    packages=['cli_anything.extreme'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-extreme=cli_anything.extreme:cli']},
)
