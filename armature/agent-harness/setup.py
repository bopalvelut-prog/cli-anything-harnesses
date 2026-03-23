from setuptools import setup
setup(
    name='cli-anything-armature',
    version='1.0.0',
    packages=['cli_anything.armature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-armature=cli_anything.armature:cli']},
)
