from setuptools import setup
setup(
    name='cli-anything-string',
    version='1.0.0',
    packages=['cli_anything.string'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-string=cli_anything.string:cli']},
)
