from setuptools import setup
setup(
    name='cli-anything-chicken',
    version='1.0.0',
    packages=['cli_anything.chicken'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chicken=cli_anything.chicken:cli']},
)
