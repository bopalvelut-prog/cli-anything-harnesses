from setuptools import setup
setup(
    name='cli-anything-antidote',
    version='1.0.0',
    packages=['cli_anything.antidote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-antidote=cli_anything.antidote:cli']},
)
