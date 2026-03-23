from setuptools import setup
setup(
    name='cli-anything-legal',
    version='1.0.0',
    packages=['cli_anything.legal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-legal=cli_anything.legal:cli']},
)
