from setuptools import setup
setup(
    name='cli-anything-margin',
    version='1.0.0',
    packages=['cli_anything.margin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-margin=cli_anything.margin:cli']},
)
