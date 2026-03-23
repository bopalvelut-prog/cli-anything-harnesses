from setuptools import setup
setup(
    name='cli-anything-replit',
    version='1.0.0',
    packages=['cli_anything.replit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-replit=cli_anything.replit:cli']},
)
