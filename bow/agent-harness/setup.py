from setuptools import setup
setup(
    name='cli-anything-bow',
    version='1.0.0',
    packages=['cli_anything.bow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bow=cli_anything.bow:cli']},
)
