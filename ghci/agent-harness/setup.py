from setuptools import setup
setup(
    name='cli-anything-ghci',
    version='1.0.0',
    packages=['cli_anything.ghci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ghci=cli_anything.ghci:cli']},
)
