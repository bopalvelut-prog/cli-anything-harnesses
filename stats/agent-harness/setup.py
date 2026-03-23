from setuptools import setup
setup(
    name='cli-anything-stats',
    version='1.0.0',
    packages=['cli_anything.stats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stats=cli_anything.stats:cli']},
)
