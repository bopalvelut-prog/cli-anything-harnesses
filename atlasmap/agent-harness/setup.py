from setuptools import setup
setup(
    name='cli-anything-atlasmap',
    version='1.0.0',
    packages=['cli_anything.atlasmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atlasmap=cli_anything.atlasmap:cli']},
)
