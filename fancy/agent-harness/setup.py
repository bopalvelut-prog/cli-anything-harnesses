from setuptools import setup
setup(
    name='cli-anything-fancy',
    version='1.0.0',
    packages=['cli_anything.fancy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fancy=cli_anything.fancy:cli']},
)
