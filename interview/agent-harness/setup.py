from setuptools import setup
setup(
    name='cli-anything-interview',
    version='1.0.0',
    packages=['cli_anything.interview'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-interview=cli_anything.interview:cli']},
)
