from setuptools import setup
setup(
    name='cli-anything-damage',
    version='1.0.0',
    packages=['cli_anything.damage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-damage=cli_anything.damage:cli']},
)
