from setuptools import setup
setup(
    name='cli-anything-more',
    version='1.0.0',
    packages=['cli_anything.more'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-more=cli_anything.more:cli']},
)
