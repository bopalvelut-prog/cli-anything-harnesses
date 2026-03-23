from setuptools import setup
setup(
    name='cli-anything-dendrite',
    version='1.0.0',
    packages=['cli_anything.dendrite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dendrite=cli_anything.dendrite:cli']},
)
