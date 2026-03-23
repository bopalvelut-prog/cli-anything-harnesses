from setuptools import setup
setup(
    name='cli-anything-head',
    version='1.0.0',
    packages=['cli_anything.head'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-head=cli_anything.head:cli']},
)
