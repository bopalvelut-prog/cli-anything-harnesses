from setuptools import setup
setup(
    name='cli-anything-mongoose',
    version='1.0.0',
    packages=['cli_anything.mongoose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mongoose=cli_anything.mongoose:cli']},
)
