from setuptools import setup
setup(
    name='cli-anything-ansistrano',
    version='1.0.0',
    packages=['cli_anything.ansistrano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ansistrano=cli_anything.ansistrano:cli']},
)
