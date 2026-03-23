from setuptools import setup
setup(
    name='cli-anything-traverse',
    version='1.0.0',
    packages=['cli_anything.traverse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-traverse=cli_anything.traverse:cli']},
)
