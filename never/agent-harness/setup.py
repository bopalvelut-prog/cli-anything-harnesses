from setuptools import setup
setup(
    name='cli-anything-never',
    version='1.0.0',
    packages=['cli_anything.never'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-never=cli_anything.never:cli']},
)
