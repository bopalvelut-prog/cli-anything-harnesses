from setuptools import setup
setup(
    name='cli-anything-middle',
    version='1.0.0',
    packages=['cli_anything.middle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-middle=cli_anything.middle:cli']},
)
