from setuptools import setup
setup(
    name='cli-anything-require',
    version='1.0.0',
    packages=['cli_anything.require'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-require=cli_anything.require:cli']},
)
