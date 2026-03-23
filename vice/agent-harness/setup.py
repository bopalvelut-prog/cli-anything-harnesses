from setuptools import setup
setup(
    name='cli-anything-vice',
    version='1.0.0',
    packages=['cli_anything.vice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vice=cli_anything.vice:cli']},
)
