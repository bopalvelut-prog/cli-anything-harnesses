from setuptools import setup
setup(
    name='cli-anything-dataclass',
    version='1.0.0',
    packages=['cli_anything.dataclass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dataclass=cli_anything.dataclass:cli']},
)
