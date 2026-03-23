from setuptools import setup
setup(
    name='cli-anything-luarocks',
    version='1.0.0',
    packages=['cli_anything.luarocks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-luarocks=cli_anything.luarocks:cli']},
)
