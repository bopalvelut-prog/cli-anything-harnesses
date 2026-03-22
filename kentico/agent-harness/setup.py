from setuptools import setup
setup(
    name='cli-anything-kentico',
    version='1.0.0',
    packages=['cli_anything.kentico'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kentico=cli_anything.kentico:cli']},
)
