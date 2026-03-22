from setuptools import setup
setup(
    name='cli-anything-wikijs',
    version='1.0.0',
    packages=['cli_anything.wikijs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wikijs=cli_anything.wikijs:cli']},
)
