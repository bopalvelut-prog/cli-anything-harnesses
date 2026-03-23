from setuptools import setup
setup(
    name='cli-anything-race',
    version='1.0.0',
    packages=['cli_anything.race'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-race=cli_anything.race:cli']},
)
