from setuptools import setup
setup(
    name='cli-anything-minecraft',
    version='1.0.0',
    packages=['cli_anything.minecraft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minecraft=cli_anything.minecraft:cli']},
)
