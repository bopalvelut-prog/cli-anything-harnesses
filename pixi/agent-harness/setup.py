from setuptools import setup
setup(
    name='cli-anything-pixi',
    version='1.0.0',
    packages=['cli_anything.pixi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pixi=cli_anything.pixi:cli']},
)
