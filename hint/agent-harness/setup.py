from setuptools import setup
setup(
    name='cli-anything-hint',
    version='1.0.0',
    packages=['cli_anything.hint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hint=cli_anything.hint:cli']},
)
