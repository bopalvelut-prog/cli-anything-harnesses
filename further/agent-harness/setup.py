from setuptools import setup
setup(
    name='cli-anything-further',
    version='1.0.0',
    packages=['cli_anything.further'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-further=cli_anything.further:cli']},
)
