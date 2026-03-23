from setuptools import setup
setup(
    name='cli-anything-mirage',
    version='1.0.0',
    packages=['cli_anything.mirage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mirage=cli_anything.mirage:cli']},
)
