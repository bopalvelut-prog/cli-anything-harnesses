from setuptools import setup
setup(
    name='cli-anything-today',
    version='1.0.0',
    packages=['cli_anything.today'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-today=cli_anything.today:cli']},
)
