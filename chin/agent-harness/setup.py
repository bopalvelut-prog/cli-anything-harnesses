from setuptools import setup
setup(
    name='cli-anything-chin',
    version='1.0.0',
    packages=['cli_anything.chin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chin=cli_anything.chin:cli']},
)
