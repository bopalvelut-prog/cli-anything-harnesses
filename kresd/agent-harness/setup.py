from setuptools import setup
setup(
    name='cli-anything-kresd',
    version='1.0.0',
    packages=['cli_anything.kresd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kresd=cli_anything.kresd:cli']},
)
