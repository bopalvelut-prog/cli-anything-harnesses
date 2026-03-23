from setuptools import setup
setup(
    name='cli-anything-wing',
    version='1.0.0',
    packages=['cli_anything.wing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wing=cli_anything.wing:cli']},
)
