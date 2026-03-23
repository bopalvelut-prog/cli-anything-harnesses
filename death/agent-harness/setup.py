from setuptools import setup
setup(
    name='cli-anything-death',
    version='1.0.0',
    packages=['cli_anything.death'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-death=cli_anything.death:cli']},
)
