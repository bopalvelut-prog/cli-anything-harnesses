from setuptools import setup
setup(
    name='cli-anything-genexus',
    version='1.0.0',
    packages=['cli_anything.genexus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-genexus=cli_anything.genexus:cli']},
)
