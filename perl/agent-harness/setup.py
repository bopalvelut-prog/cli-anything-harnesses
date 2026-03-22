from setuptools import setup
setup(
    name='cli-anything-perl',
    version='1.0.0',
    packages=['cli_anything.perl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perl=cli_anything.perl:cli']},
)
