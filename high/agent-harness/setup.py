from setuptools import setup
setup(
    name='cli-anything-high',
    version='1.0.0',
    packages=['cli_anything.high'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-high=cli_anything.high:cli']},
)
