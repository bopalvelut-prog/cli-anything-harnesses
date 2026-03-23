from setuptools import setup
setup(
    name='cli-anything-serf',
    version='1.0.0',
    packages=['cli_anything.serf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serf=cli_anything.serf:cli']},
)
