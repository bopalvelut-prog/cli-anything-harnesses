from setuptools import setup
setup(
    name='cli-anything-scientist',
    version='1.0.0',
    packages=['cli_anything.scientist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scientist=cli_anything.scientist:cli']},
)
