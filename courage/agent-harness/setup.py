from setuptools import setup
setup(
    name='cli-anything-courage',
    version='1.0.0',
    packages=['cli_anything.courage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-courage=cli_anything.courage:cli']},
)
