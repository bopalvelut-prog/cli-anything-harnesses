from setuptools import setup
setup(
    name='cli-anything-little',
    version='1.0.0',
    packages=['cli_anything.little'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-little=cli_anything.little:cli']},
)
