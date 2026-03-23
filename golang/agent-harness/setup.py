from setuptools import setup
setup(
    name='cli-anything-golang',
    version='1.0.0',
    packages=['cli_anything.golang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-golang=cli_anything.golang:cli']},
)
