from setuptools import setup
setup(
    name='cli-anything-jupyter',
    version='1.0.0',
    packages=['cli_anything.jupyter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jupyter=cli_anything.jupyter:cli']},
)
