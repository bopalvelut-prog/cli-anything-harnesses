from setuptools import setup
setup(
    name='cli-anything-deepstream',
    version='1.0.0',
    packages=['cli_anything.deepstream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepstream=cli_anything.deepstream:cli']},
)
