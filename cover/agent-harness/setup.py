from setuptools import setup
setup(
    name='cli-anything-cover',
    version='1.0.0',
    packages=['cli_anything.cover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cover=cli_anything.cover:cli']},
)
