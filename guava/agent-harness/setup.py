from setuptools import setup
setup(
    name='cli-anything-guava',
    version='1.0.0',
    packages=['cli_anything.guava'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guava=cli_anything.guava:cli']},
)
