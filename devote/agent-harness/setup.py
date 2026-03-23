from setuptools import setup
setup(
    name='cli-anything-devote',
    version='1.0.0',
    packages=['cli_anything.devote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devote=cli_anything.devote:cli']},
)
