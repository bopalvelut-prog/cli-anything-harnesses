from setuptools import setup
setup(
    name='cli-anything-spacevim',
    version='1.0.0',
    packages=['cli_anything.spacevim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spacevim=cli_anything.spacevim:cli']},
)
