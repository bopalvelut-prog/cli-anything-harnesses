from setuptools import setup
setup(
    name='cli-anything-haskell',
    version='1.0.0',
    packages=['cli_anything.haskell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-haskell=cli_anything.haskell:cli']},
)
