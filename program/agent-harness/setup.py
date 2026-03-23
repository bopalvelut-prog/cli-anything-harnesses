from setuptools import setup
setup(
    name='cli-anything-program',
    version='1.0.0',
    packages=['cli_anything.program'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-program=cli_anything.program:cli']},
)
