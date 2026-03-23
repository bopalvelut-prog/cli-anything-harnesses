from setuptools import setup
setup(
    name='cli-anything-big',
    version='1.0.0',
    packages=['cli_anything.big'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-big=cli_anything.big:cli']},
)
