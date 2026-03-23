from setuptools import setup
setup(
    name='cli-anything-raid',
    version='1.0.0',
    packages=['cli_anything.raid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raid=cli_anything.raid:cli']},
)
