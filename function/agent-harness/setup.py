from setuptools import setup
setup(
    name='cli-anything-function',
    version='1.0.0',
    packages=['cli_anything.function'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-function=cli_anything.function:cli']},
)
