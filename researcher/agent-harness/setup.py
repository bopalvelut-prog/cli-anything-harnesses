from setuptools import setup
setup(
    name='cli-anything-researcher',
    version='1.0.0',
    packages=['cli_anything.researcher'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-researcher=cli_anything.researcher:cli']},
)
