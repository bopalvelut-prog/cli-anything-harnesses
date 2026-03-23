from setuptools import setup
setup(
    name='cli-anything-anthropic',
    version='1.0.0',
    packages=['cli_anything.anthropic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anthropic=cli_anything.anthropic:cli']},
)
