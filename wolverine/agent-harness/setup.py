from setuptools import setup
setup(
    name='cli-anything-wolverine',
    version='1.0.0',
    packages=['cli_anything.wolverine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wolverine=cli_anything.wolverine:cli']},
)
