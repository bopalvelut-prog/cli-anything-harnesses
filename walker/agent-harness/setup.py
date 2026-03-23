from setuptools import setup
setup(
    name='cli-anything-walker',
    version='1.0.0',
    packages=['cli_anything.walker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-walker=cli_anything.walker:cli']},
)
