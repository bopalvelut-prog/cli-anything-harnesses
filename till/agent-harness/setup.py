from setuptools import setup
setup(
    name='cli-anything-till',
    version='1.0.0',
    packages=['cli_anything.till'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-till=cli_anything.till:cli']},
)
