from setuptools import setup
setup(
    name='cli-anything-threaten',
    version='1.0.0',
    packages=['cli_anything.threaten'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-threaten=cli_anything.threaten:cli']},
)
