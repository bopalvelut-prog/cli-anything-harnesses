from setuptools import setup
setup(
    name='cli-anything-capistrano',
    version='1.0.0',
    packages=['cli_anything.capistrano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capistrano=cli_anything.capistrano:cli']},
)
