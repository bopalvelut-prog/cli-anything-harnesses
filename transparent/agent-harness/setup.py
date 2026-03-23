from setuptools import setup
setup(
    name='cli-anything-transparent',
    version='1.0.0',
    packages=['cli_anything.transparent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transparent=cli_anything.transparent:cli']},
)
