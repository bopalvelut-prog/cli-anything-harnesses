from setuptools import setup
setup(
    name='cli-anything-cycle',
    version='1.0.0',
    packages=['cli_anything.cycle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cycle=cli_anything.cycle:cli']},
)
