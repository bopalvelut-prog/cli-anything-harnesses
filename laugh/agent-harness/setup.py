from setuptools import setup
setup(
    name='cli-anything-laugh',
    version='1.0.0',
    packages=['cli_anything.laugh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-laugh=cli_anything.laugh:cli']},
)
