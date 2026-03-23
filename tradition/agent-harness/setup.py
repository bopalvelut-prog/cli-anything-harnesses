from setuptools import setup
setup(
    name='cli-anything-tradition',
    version='1.0.0',
    packages=['cli_anything.tradition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tradition=cli_anything.tradition:cli']},
)
