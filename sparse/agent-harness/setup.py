from setuptools import setup
setup(
    name='cli-anything-sparse',
    version='1.0.0',
    packages=['cli_anything.sparse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sparse=cli_anything.sparse:cli']},
)
