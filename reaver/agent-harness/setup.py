from setuptools import setup
setup(
    name='cli-anything-reaver',
    version='1.0.0',
    packages=['cli_anything.reaver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reaver=cli_anything.reaver:cli']},
)
