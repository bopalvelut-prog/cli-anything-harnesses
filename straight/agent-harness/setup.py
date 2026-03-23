from setuptools import setup
setup(
    name='cli-anything-straight',
    version='1.0.0',
    packages=['cli_anything.straight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-straight=cli_anything.straight:cli']},
)
