from setuptools import setup
setup(
    name='cli-anything-habit',
    version='1.0.0',
    packages=['cli_anything.habit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-habit=cli_anything.habit:cli']},
)
