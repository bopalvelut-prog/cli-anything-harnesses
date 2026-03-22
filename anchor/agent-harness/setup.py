from setuptools import setup
setup(
    name='cli-anything-anchor',
    version='1.0.0',
    packages=['cli_anything.anchor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anchor=cli_anything.anchor:cli']},
)
