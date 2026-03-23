from setuptools import setup
setup(
    name='cli-anything-parsec',
    version='1.0.0',
    packages=['cli_anything.parsec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parsec=cli_anything.parsec:cli']},
)
