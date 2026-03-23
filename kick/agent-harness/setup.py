from setuptools import setup
setup(
    name='cli-anything-kick',
    version='1.0.0',
    packages=['cli_anything.kick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kick=cli_anything.kick:cli']},
)
