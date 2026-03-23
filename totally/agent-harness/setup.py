from setuptools import setup
setup(
    name='cli-anything-totally',
    version='1.0.0',
    packages=['cli_anything.totally'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-totally=cli_anything.totally:cli']},
)
