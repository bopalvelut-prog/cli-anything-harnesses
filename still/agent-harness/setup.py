from setuptools import setup
setup(
    name='cli-anything-still',
    version='1.0.0',
    packages=['cli_anything.still'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-still=cli_anything.still:cli']},
)
