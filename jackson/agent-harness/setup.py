from setuptools import setup
setup(
    name='cli-anything-jackson',
    version='1.0.0',
    packages=['cli_anything.jackson'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jackson=cli_anything.jackson:cli']},
)
