from setuptools import setup
setup(
    name='cli-anything-world',
    version='1.0.0',
    packages=['cli_anything.world'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-world=cli_anything.world:cli']},
)
