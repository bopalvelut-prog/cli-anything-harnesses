from setuptools import setup
setup(
    name='cli-anything-jsr',
    version='1.0.0',
    packages=['cli_anything.jsr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsr=cli_anything.jsr:cli']},
)
