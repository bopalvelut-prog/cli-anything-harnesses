from setuptools import setup
setup(
    name='cli-anything-activestorage',
    version='1.0.0',
    packages=['cli_anything.activestorage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activestorage=cli_anything.activestorage:cli']},
)
