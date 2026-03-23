from setuptools import setup
setup(
    name='cli-anything-pylint',
    version='1.0.0',
    packages=['cli_anything.pylint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pylint=cli_anything.pylint:cli']},
)
