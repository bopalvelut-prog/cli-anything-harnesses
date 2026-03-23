from setuptools import setup
setup(
    name='cli-anything-carry',
    version='1.0.0',
    packages=['cli_anything.carry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carry=cli_anything.carry:cli']},
)
