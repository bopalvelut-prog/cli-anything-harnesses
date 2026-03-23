from setuptools import setup
setup(
    name='cli-anything-prctl',
    version='1.0.0',
    packages=['cli_anything.prctl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prctl=cli_anything.prctl:cli']},
)
