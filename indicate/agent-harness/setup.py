from setuptools import setup
setup(
    name='cli-anything-indicate',
    version='1.0.0',
    packages=['cli_anything.indicate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-indicate=cli_anything.indicate:cli']},
)
