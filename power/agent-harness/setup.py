from setuptools import setup
setup(
    name='cli-anything-power',
    version='1.0.0',
    packages=['cli_anything.power'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-power=cli_anything.power:cli']},
)
