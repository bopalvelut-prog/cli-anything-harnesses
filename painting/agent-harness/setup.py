from setuptools import setup
setup(
    name='cli-anything-painting',
    version='1.0.0',
    packages=['cli_anything.painting'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-painting=cli_anything.painting:cli']},
)
