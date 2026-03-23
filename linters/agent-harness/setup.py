from setuptools import setup
setup(
    name='cli-anything-linters',
    version='1.0.0',
    packages=['cli_anything.linters'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linters=cli_anything.linters:cli']},
)
