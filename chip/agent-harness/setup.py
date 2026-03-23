from setuptools import setup
setup(
    name='cli-anything-chip',
    version='1.0.0',
    packages=['cli_anything.chip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chip=cli_anything.chip:cli']},
)
