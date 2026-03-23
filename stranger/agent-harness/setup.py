from setuptools import setup
setup(
    name='cli-anything-stranger',
    version='1.0.0',
    packages=['cli_anything.stranger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stranger=cli_anything.stranger:cli']},
)
