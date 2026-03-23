from setuptools import setup
setup(
    name='cli-anything-formal',
    version='1.0.0',
    packages=['cli_anything.formal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formal=cli_anything.formal:cli']},
)
