from setuptools import setup
setup(
    name='cli-anything-troll',
    version='1.0.0',
    packages=['cli_anything.troll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-troll=cli_anything.troll:cli']},
)
