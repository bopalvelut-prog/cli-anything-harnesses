from setuptools import setup
setup(
    name='cli-anything-multitail',
    version='1.0.0',
    packages=['cli_anything.multitail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-multitail=cli_anything.multitail:cli']},
)
