from setuptools import setup
setup(
    name='cli-anything-alpine',
    version='1.0.0',
    packages=['cli_anything.alpine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alpine=cli_anything.alpine:cli']},
)
