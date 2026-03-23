from setuptools import setup
setup(
    name='cli-anything-toe',
    version='1.0.0',
    packages=['cli_anything.toe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toe=cli_anything.toe:cli']},
)
