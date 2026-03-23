from setuptools import setup
setup(
    name='cli-anything-turbopack',
    version='1.0.0',
    packages=['cli_anything.turbopack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turbopack=cli_anything.turbopack:cli']},
)
