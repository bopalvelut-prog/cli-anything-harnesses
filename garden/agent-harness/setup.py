from setuptools import setup
setup(
    name='cli-anything-garden',
    version='1.0.0',
    packages=['cli_anything.garden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-garden=cli_anything.garden:cli']},
)
