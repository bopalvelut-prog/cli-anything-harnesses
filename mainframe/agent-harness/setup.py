from setuptools import setup
setup(
    name='cli-anything-mainframe',
    version='1.0.0',
    packages=['cli_anything.mainframe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mainframe=cli_anything.mainframe:cli']},
)
