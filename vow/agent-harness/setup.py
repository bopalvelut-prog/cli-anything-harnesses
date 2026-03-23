from setuptools import setup
setup(
    name='cli-anything-vow',
    version='1.0.0',
    packages=['cli_anything.vow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vow=cli_anything.vow:cli']},
)
