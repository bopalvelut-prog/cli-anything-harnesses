from setuptools import setup
setup(
    name='cli-anything-xlsx',
    version='1.0.0',
    packages=['cli_anything.xlsx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xlsx=cli_anything.xlsx:cli']},
)
