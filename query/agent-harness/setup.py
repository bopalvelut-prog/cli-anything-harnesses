from setuptools import setup
setup(
    name='cli-anything-query',
    version='1.0.0',
    packages=['cli_anything.query'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-query=cli_anything.query:cli']},
)
