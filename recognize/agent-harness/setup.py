from setuptools import setup
setup(
    name='cli-anything-recognize',
    version='1.0.0',
    packages=['cli_anything.recognize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recognize=cli_anything.recognize:cli']},
)
