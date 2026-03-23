from setuptools import setup
setup(
    name='cli-anything-wooden',
    version='1.0.0',
    packages=['cli_anything.wooden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wooden=cli_anything.wooden:cli']},
)
