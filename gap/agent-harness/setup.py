from setuptools import setup
setup(
    name='cli-anything-gap',
    version='1.0.0',
    packages=['cli_anything.gap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gap=cli_anything.gap:cli']},
)
