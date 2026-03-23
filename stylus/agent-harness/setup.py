from setuptools import setup
setup(
    name='cli-anything-stylus',
    version='1.0.0',
    packages=['cli_anything.stylus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stylus=cli_anything.stylus:cli']},
)
