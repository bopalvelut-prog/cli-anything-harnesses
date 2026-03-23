from setuptools import setup
setup(
    name='cli-anything-ember',
    version='1.0.0',
    packages=['cli_anything.ember'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ember=cli_anything.ember:cli']},
)
