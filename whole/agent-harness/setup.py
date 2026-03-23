from setuptools import setup
setup(
    name='cli-anything-whole',
    version='1.0.0',
    packages=['cli_anything.whole'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whole=cli_anything.whole:cli']},
)
