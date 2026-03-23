from setuptools import setup
setup(
    name='cli-anything-dotfiles',
    version='1.0.0',
    packages=['cli_anything.dotfiles'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dotfiles=cli_anything.dotfiles:cli']},
)
