from setuptools import setup
setup(
    name='cli-anything-noble',
    version='1.0.0',
    packages=['cli_anything.noble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-noble=cli_anything.noble:cli']},
)
