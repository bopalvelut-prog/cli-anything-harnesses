from setuptools import setup
setup(
    name='cli-anything-someone',
    version='1.0.0',
    packages=['cli_anything.someone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-someone=cli_anything.someone:cli']},
)
