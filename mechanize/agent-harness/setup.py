from setuptools import setup
setup(
    name='cli-anything-mechanize',
    version='1.0.0',
    packages=['cli_anything.mechanize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mechanize=cli_anything.mechanize:cli']},
)
