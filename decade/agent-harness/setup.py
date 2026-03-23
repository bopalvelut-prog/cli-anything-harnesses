from setuptools import setup
setup(
    name='cli-anything-decade',
    version='1.0.0',
    packages=['cli_anything.decade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decade=cli_anything.decade:cli']},
)
