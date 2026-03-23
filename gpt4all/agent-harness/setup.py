from setuptools import setup
setup(
    name='cli-anything-gpt4all',
    version='1.0.0',
    packages=['cli_anything.gpt4all'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gpt4all=cli_anything.gpt4all:cli']},
)
