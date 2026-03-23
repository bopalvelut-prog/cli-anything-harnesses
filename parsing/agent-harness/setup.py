from setuptools import setup
setup(
    name='cli-anything-parsing',
    version='1.0.0',
    packages=['cli_anything.parsing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parsing=cli_anything.parsing:cli']},
)
