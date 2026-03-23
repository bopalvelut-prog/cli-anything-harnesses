from setuptools import setup
setup(
    name='cli-anything-employ',
    version='1.0.0',
    packages=['cli_anything.employ'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-employ=cli_anything.employ:cli']},
)
