from setuptools import setup
setup(
    name='cli-anything-nokia',
    version='1.0.0',
    packages=['cli_anything.nokia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nokia=cli_anything.nokia:cli']},
)
