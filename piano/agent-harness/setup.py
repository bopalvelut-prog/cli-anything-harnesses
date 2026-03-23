from setuptools import setup
setup(
    name='cli-anything-piano',
    version='1.0.0',
    packages=['cli_anything.piano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-piano=cli_anything.piano:cli']},
)
