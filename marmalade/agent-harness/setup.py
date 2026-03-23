from setuptools import setup
setup(
    name='cli-anything-marmalade',
    version='1.0.0',
    packages=['cli_anything.marmalade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marmalade=cli_anything.marmalade:cli']},
)
