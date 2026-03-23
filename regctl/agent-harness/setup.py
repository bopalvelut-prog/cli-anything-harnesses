from setuptools import setup
setup(
    name='cli-anything-regctl',
    version='1.0.0',
    packages=['cli_anything.regctl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regctl=cli_anything.regctl:cli']},
)
