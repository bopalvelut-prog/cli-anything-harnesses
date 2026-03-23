from setuptools import setup
setup(
    name='cli-anything-nerve',
    version='1.0.0',
    packages=['cli_anything.nerve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nerve=cli_anything.nerve:cli']},
)
