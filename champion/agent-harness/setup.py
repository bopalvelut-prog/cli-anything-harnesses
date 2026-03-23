from setuptools import setup
setup(
    name='cli-anything-champion',
    version='1.0.0',
    packages=['cli_anything.champion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-champion=cli_anything.champion:cli']},
)
