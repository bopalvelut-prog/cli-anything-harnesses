from setuptools import setup
setup(
    name='cli-anything-thegraph',
    version='1.0.0',
    packages=['cli_anything.thegraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thegraph=cli_anything.thegraph:cli']},
)
