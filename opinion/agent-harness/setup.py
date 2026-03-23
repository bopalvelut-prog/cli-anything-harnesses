from setuptools import setup
setup(
    name='cli-anything-opinion',
    version='1.0.0',
    packages=['cli_anything.opinion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opinion=cli_anything.opinion:cli']},
)
