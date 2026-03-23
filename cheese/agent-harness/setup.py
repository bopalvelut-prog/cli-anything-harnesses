from setuptools import setup
setup(
    name='cli-anything-cheese',
    version='1.0.0',
    packages=['cli_anything.cheese'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cheese=cli_anything.cheese:cli']},
)
