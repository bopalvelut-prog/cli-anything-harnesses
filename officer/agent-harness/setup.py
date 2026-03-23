from setuptools import setup
setup(
    name='cli-anything-officer',
    version='1.0.0',
    packages=['cli_anything.officer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-officer=cli_anything.officer:cli']},
)
