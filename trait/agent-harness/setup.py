from setuptools import setup
setup(
    name='cli-anything-trait',
    version='1.0.0',
    packages=['cli_anything.trait'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trait=cli_anything.trait:cli']},
)
