from setuptools import setup
setup(
    name='cli-anything-much',
    version='1.0.0',
    packages=['cli_anything.much'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-much=cli_anything.much:cli']},
)
