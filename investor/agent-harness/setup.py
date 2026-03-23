from setuptools import setup
setup(
    name='cli-anything-investor',
    version='1.0.0',
    packages=['cli_anything.investor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-investor=cli_anything.investor:cli']},
)
