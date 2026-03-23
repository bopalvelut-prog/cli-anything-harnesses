from setuptools import setup
setup(
    name='cli-anything-fifty',
    version='1.0.0',
    packages=['cli_anything.fifty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fifty=cli_anything.fifty:cli']},
)
