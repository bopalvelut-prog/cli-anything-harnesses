from setuptools import setup
setup(
    name='cli-anything-sort',
    version='1.0.0',
    packages=['cli_anything.sort'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sort=cli_anything.sort:cli']},
)
