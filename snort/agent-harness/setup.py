from setuptools import setup
setup(
    name='cli-anything-snort',
    version='1.0.0',
    packages=['cli_anything.snort'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snort=cli_anything.snort:cli']},
)
