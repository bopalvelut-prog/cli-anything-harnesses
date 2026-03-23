from setuptools import setup
setup(
    name='cli-anything-myself',
    version='1.0.0',
    packages=['cli_anything.myself'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-myself=cli_anything.myself:cli']},
)
