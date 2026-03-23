from setuptools import setup
setup(
    name='cli-anything-steel',
    version='1.0.0',
    packages=['cli_anything.steel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steel=cli_anything.steel:cli']},
)
