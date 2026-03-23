from setuptools import setup
setup(
    name='cli-anything-counter',
    version='1.0.0',
    packages=['cli_anything.counter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-counter=cli_anything.counter:cli']},
)
