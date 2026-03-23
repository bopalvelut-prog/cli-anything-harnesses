from setuptools import setup
setup(
    name='cli-anything-cfssl',
    version='1.0.0',
    packages=['cli_anything.cfssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cfssl=cli_anything.cfssl:cli']},
)
