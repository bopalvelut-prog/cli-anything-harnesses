from setuptools import setup
setup(
    name='cli-anything-crush',
    version='1.0.0',
    packages=['cli_anything.crush'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crush=cli_anything.crush:cli']},
)
