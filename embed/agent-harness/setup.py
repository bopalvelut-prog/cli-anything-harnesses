from setuptools import setup
setup(
    name='cli-anything-embed',
    version='1.0.0',
    packages=['cli_anything.embed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-embed=cli_anything.embed:cli']},
)
