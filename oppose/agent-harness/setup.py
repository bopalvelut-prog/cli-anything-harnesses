from setuptools import setup
setup(
    name='cli-anything-oppose',
    version='1.0.0',
    packages=['cli_anything.oppose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oppose=cli_anything.oppose:cli']},
)
