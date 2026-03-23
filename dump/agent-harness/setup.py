from setuptools import setup
setup(
    name='cli-anything-dump',
    version='1.0.0',
    packages=['cli_anything.dump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dump=cli_anything.dump:cli']},
)
