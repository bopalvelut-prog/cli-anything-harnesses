from setuptools import setup
setup(
    name='cli-anything-bronze',
    version='1.0.0',
    packages=['cli_anything.bronze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bronze=cli_anything.bronze:cli']},
)
