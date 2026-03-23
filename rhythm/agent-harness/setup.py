from setuptools import setup
setup(
    name='cli-anything-rhythm',
    version='1.0.0',
    packages=['cli_anything.rhythm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rhythm=cli_anything.rhythm:cli']},
)
