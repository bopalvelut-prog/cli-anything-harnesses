from setuptools import setup
setup(
    name='cli-anything-person',
    version='1.0.0',
    packages=['cli_anything.person'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-person=cli_anything.person:cli']},
)
