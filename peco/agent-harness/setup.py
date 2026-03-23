from setuptools import setup
setup(
    name='cli-anything-peco',
    version='1.0.0',
    packages=['cli_anything.peco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peco=cli_anything.peco:cli']},
)
