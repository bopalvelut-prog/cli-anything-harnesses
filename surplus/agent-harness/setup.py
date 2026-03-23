from setuptools import setup
setup(
    name='cli-anything-surplus',
    version='1.0.0',
    packages=['cli_anything.surplus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surplus=cli_anything.surplus:cli']},
)
