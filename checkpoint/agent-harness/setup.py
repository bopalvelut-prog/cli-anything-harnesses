from setuptools import setup
setup(
    name='cli-anything-checkpoint',
    version='1.0.0',
    packages=['cli_anything.checkpoint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-checkpoint=cli_anything.checkpoint:cli']},
)
