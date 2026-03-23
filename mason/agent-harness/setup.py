from setuptools import setup
setup(
    name='cli-anything-mason',
    version='1.0.0',
    packages=['cli_anything.mason'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mason=cli_anything.mason:cli']},
)
