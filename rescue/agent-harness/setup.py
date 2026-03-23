from setuptools import setup
setup(
    name='cli-anything-rescue',
    version='1.0.0',
    packages=['cli_anything.rescue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rescue=cli_anything.rescue:cli']},
)
