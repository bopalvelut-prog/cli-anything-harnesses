from setuptools import setup
setup(
    name='cli-anything-theory',
    version='1.0.0',
    packages=['cli_anything.theory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-theory=cli_anything.theory:cli']},
)
