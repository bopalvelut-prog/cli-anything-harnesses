from setuptools import setup
setup(
    name='cli-anything-win',
    version='1.0.0',
    packages=['cli_anything.win'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-win=cli_anything.win:cli']},
)
