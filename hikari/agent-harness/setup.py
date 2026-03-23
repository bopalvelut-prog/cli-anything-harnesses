from setuptools import setup
setup(
    name='cli-anything-hikari',
    version='1.0.0',
    packages=['cli_anything.hikari'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hikari=cli_anything.hikari:cli']},
)
