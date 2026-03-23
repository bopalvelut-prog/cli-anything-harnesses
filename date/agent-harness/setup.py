from setuptools import setup
setup(
    name='cli-anything-date',
    version='1.0.0',
    packages=['cli_anything.date'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-date=cli_anything.date:cli']},
)
