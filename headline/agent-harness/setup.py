from setuptools import setup
setup(
    name='cli-anything-headline',
    version='1.0.0',
    packages=['cli_anything.headline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-headline=cli_anything.headline:cli']},
)
