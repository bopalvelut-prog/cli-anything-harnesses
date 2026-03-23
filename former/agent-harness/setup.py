from setuptools import setup
setup(
    name='cli-anything-former',
    version='1.0.0',
    packages=['cli_anything.former'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-former=cli_anything.former:cli']},
)
