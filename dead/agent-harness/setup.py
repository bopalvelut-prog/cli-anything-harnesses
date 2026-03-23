from setuptools import setup
setup(
    name='cli-anything-dead',
    version='1.0.0',
    packages=['cli_anything.dead'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dead=cli_anything.dead:cli']},
)
