from setuptools import setup
setup(
    name='cli-anything-window',
    version='1.0.0',
    packages=['cli_anything.window'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-window=cli_anything.window:cli']},
)
