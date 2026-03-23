from setuptools import setup
setup(
    name='cli-anything-fastly',
    version='1.0.0',
    packages=['cli_anything.fastly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fastly=cli_anything.fastly:cli']},
)
