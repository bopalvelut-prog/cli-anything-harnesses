from setuptools import setup
setup(
    name='cli-anything-statistics',
    version='1.0.0',
    packages=['cli_anything.statistics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-statistics=cli_anything.statistics:cli']},
)
