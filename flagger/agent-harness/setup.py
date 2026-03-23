from setuptools import setup
setup(
    name='cli-anything-flagger',
    version='1.0.0',
    packages=['cli_anything.flagger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flagger=cli_anything.flagger:cli']},
)
