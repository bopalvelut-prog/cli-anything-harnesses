from setuptools import setup
setup(
    name='cli-anything-lawn',
    version='1.0.0',
    packages=['cli_anything.lawn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lawn=cli_anything.lawn:cli']},
)
