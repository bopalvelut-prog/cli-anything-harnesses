from setuptools import setup
setup(
    name='cli-anything-french',
    version='1.0.0',
    packages=['cli_anything.french'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-french=cli_anything.french:cli']},
)
