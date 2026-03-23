from setuptools import setup
setup(
    name='cli-anything-dedupe',
    version='1.0.0',
    packages=['cli_anything.dedupe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dedupe=cli_anything.dedupe:cli']},
)
