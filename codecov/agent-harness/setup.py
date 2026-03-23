from setuptools import setup
setup(
    name='cli-anything-codecov',
    version='1.0.0',
    packages=['cli_anything.codecov'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codecov=cli_anything.codecov:cli']},
)
