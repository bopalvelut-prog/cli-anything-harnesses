from setuptools import setup
setup(
    name='cli-anything-valuable',
    version='1.0.0',
    packages=['cli_anything.valuable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-valuable=cli_anything.valuable:cli']},
)
