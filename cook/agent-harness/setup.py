from setuptools import setup
setup(
    name='cli-anything-cook',
    version='1.0.0',
    packages=['cli_anything.cook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cook=cli_anything.cook:cli']},
)
