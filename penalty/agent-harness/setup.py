from setuptools import setup
setup(
    name='cli-anything-penalty',
    version='1.0.0',
    packages=['cli_anything.penalty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-penalty=cli_anything.penalty:cli']},
)
