from setuptools import setup
setup(
    name='cli-anything-virtue',
    version='1.0.0',
    packages=['cli_anything.virtue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-virtue=cli_anything.virtue:cli']},
)
