from setuptools import setup
setup(
    name='cli-anything-cheap',
    version='1.0.0',
    packages=['cli_anything.cheap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cheap=cli_anything.cheap:cli']},
)
