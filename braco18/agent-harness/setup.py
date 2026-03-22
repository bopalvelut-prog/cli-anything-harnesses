from setuptools import setup
setup(
    name='cli-anything-braco18',
    version='1.0.0',
    packages=['cli_anything.braco18'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco18=cli_anything.braco18:cli']},
)
