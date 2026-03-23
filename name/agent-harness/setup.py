from setuptools import setup
setup(
    name='cli-anything-name',
    version='1.0.0',
    packages=['cli_anything.name'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-name=cli_anything.name:cli']},
)
