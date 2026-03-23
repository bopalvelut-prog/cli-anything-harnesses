from setuptools import setup
setup(
    name='cli-anything-x',
    version='1.0.0',
    packages=['cli_anything.x'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-x=cli_anything.x:cli']},
)
