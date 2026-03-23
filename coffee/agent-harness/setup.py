from setuptools import setup
setup(
    name='cli-anything-coffee',
    version='1.0.0',
    packages=['cli_anything.coffee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coffee=cli_anything.coffee:cli']},
)
