from setuptools import setup
setup(
    name='cli-anything-starch',
    version='1.0.0',
    packages=['cli_anything.starch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-starch=cli_anything.starch:cli']},
)
