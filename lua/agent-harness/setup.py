from setuptools import setup
setup(
    name='cli-anything-lua',
    version='1.0.0',
    packages=['cli_anything.lua'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lua=cli_anything.lua:cli']},
)
