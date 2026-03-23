from setuptools import setup
setup(
    name='cli-anything-joke',
    version='1.0.0',
    packages=['cli_anything.joke'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joke=cli_anything.joke:cli']},
)
