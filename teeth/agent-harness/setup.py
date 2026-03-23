from setuptools import setup
setup(
    name='cli-anything-teeth',
    version='1.0.0',
    packages=['cli_anything.teeth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teeth=cli_anything.teeth:cli']},
)
