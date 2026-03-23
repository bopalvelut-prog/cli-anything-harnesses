from setuptools import setup
setup(
    name='cli-anything-timeline',
    version='1.0.0',
    packages=['cli_anything.timeline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timeline=cli_anything.timeline:cli']},
)
