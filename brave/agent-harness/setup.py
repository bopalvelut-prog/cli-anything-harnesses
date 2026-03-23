from setuptools import setup
setup(
    name='cli-anything-brave',
    version='1.0.0',
    packages=['cli_anything.brave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brave=cli_anything.brave:cli']},
)
