from setuptools import setup
setup(
    name='cli-anything-powder',
    version='1.0.0',
    packages=['cli_anything.powder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-powder=cli_anything.powder:cli']},
)
