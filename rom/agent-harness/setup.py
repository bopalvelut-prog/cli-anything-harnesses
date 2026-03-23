from setuptools import setup
setup(
    name='cli-anything-rom',
    version='1.0.0',
    packages=['cli_anything.rom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rom=cli_anything.rom:cli']},
)
