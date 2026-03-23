from setuptools import setup
setup(
    name='cli-anything-island',
    version='1.0.0',
    packages=['cli_anything.island'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-island=cli_anything.island:cli']},
)
