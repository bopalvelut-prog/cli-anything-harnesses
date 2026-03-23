from setuptools import setup
setup(
    name='cli-anything-tabulate',
    version='1.0.0',
    packages=['cli_anything.tabulate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tabulate=cli_anything.tabulate:cli']},
)
