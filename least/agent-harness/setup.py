from setuptools import setup
setup(
    name='cli-anything-least',
    version='1.0.0',
    packages=['cli_anything.least'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-least=cli_anything.least:cli']},
)
