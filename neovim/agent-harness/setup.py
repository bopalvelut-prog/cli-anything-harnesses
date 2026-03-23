from setuptools import setup
setup(
    name='cli-anything-neovim',
    version='1.0.0',
    packages=['cli_anything.neovim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neovim=cli_anything.neovim:cli']},
)
