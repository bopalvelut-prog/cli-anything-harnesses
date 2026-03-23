from setuptools import setup
setup(
    name='cli-anything-combat',
    version='1.0.0',
    packages=['cli_anything.combat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-combat=cli_anything.combat:cli']},
)
