from setuptools import setup
setup(
    name='cli-anything-touch',
    version='1.0.0',
    packages=['cli_anything.touch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-touch=cli_anything.touch:cli']},
)
