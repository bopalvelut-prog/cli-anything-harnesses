from setuptools import setup
setup(
    name='cli-anything-armory',
    version='1.0.0',
    packages=['cli_anything.armory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-armory=cli_anything.armory:cli']},
)
